%define	major	8
%define	libname	%mklibname ksba %{major}
%define	devname	%mklibname ksba -d

Summary:	Library handling X.509 certificates and CMS data
Name:		libksba
Version:	1.3.0
Release:	11
License:	GPLv3
Group:		System/Libraries
Url:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:	pkgconfig(gpg-error)

%description
KSBA is a library designed to build software based on the X.509 and CMS 
protocols.

%package -n	%{libname}
Summary:	Library handling X.509 certificates and CMS data
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
KSBA is a library designed to build software based on the X.509 and CMS
 protocols.

%package -n	%{devname}
Summary:	Development files for %{name} package
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains files needed to develop applications using %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/ksba-config

%check
%make check

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README THANKS TODO
%{multiarch_bindir}/ksba-config
%{_bindir}/ksba-config
%{_datadir}/aclocal/*
%{_includedir}/*.h
%{_infodir}/*.info*
%{_libdir}/*.so

