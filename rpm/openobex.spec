Name:       openobex
Summary:    Library for using OBEX
Version:    1.5
Release:    1
License:    GPLv2+
URL:        http://openobex.org
Source0:    http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
Patch0:     fix-the-cmd-code-when-delivering.patch
Patch1:     001_null_check.patch
Patch2:     ensure-socket-buffer-size.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libusb)
BuildRequires:  autoconf
BuildRequires:  sed
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
Open OBEX shared c-library

%package devel
Summary:    Files for development of applications which will use OBEX
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   bluez-libs-devel

%description devel
Open OBEX shared c-library

%prep
%setup -q -n %{name}-%{version}/openobex

# fix-the-cmd-code-when-delivering.patch
%patch0 -p1
# 001_null_check.patch
%patch1 -p1
# ensure-socket-buffer-size.patch
%patch2 -p1

%build
./bootstrap

%configure --disable-static \
    --enable-usb \
    --disable-bluetooth \
    --disable-apps

%make_build

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB ChangeLog README
%{_libdir}/libopenobex*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libopenobex*.so
%dir %{_includedir}/openobex
%{_includedir}/openobex/*.h
%{_libdir}/pkgconfig/openobex.pc
