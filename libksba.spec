%define major   8
%define libname %mklibname ksba %{major}

Summary:        Library handling X.509 certificates and CMS data
Name:           libksba
Version:        1.0.2
Release:        %mkrel 1
License:        GPLv3
Group:          System/Libraries
URL:            http://www.gnupg.org/
Source0:        ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:  libgpg-error-devel >= 1.2
%if %mdkversion >= 1020
BuildRequires:  multiarch-utils >= 1.0.3
%endif

%description
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

%package -n %{libname}
Summary:        Library handling X.509 certificates and CMS data
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

%package -n %{libname}-devel
Summary:        Development files for %{name} package
Group:          Development/Other
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

This package contains files needed to develop
applications using %{name} (For example Ägypten project).

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/ksba-config
%endif

%check
%{__make} check

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
%_install_info %{name}.info

%postun -n %{libname}-devel
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README THANKS TODO
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/ksba-config
%endif
%{_bindir}/ksba-config
%{_datadir}/aclocal/*
%{_includedir}/*.h
%{_infodir}/*.info*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so


