%define major 8
%define libname %mklibname ksba %{major}
%define develname %mklibname ksba -d

Summary:        Library handling X.509 certificates and CMS data
Name:           libksba
Version:        1.0.7
Release:        %mkrel 2
License:        GPLv3
Group:          System/Libraries
URL:            http://www.gnupg.org/
Source0:        ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:  libgpg-error-devel >= 1.2
BuildRequires:  multiarch-utils >= 1.0.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

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

%package -n %{develname}
Summary:        Development files for %{name} package
Group:          Development/Other
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname ksba 8 -d

%description -n %{develname}
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

This package contains files needed to develop
applications using %{name} (For example Ägypten project).

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/ksba-config


%check
%make check

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{develname}
%_install_info %{name}.info

%postun -n %{develname}
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README THANKS TODO
%multiarch %{multiarch_bindir}/ksba-config
%{_bindir}/ksba-config
%{_datadir}/aclocal/*
%{_includedir}/*.h
%{_infodir}/*.info*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
