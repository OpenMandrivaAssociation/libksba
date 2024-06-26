%define major 8
%define oldlibname %mklibname ksba 8
%define libname %mklibname ksba
%define devname %mklibname ksba -d

Summary:	Library handling X.509 certificates and CMS data
Name:		libksba
Version:	1.6.7
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		http://www.gnupg.org/
Source0:	https://www.gnupg.org/ftp/gcrypt/libksba/libksba-%{version}.tar.bz2
BuildRequires:	pkgconfig(gpg-error)
BuildSystem:	autotools

%description
KSBA is a library designed to build software based on the X.509 and CMS 
protocols.

%package -n %{libname}
Summary:	Library handling X.509 certificates and CMS data
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
# Fixed after 5.0
%rename %{oldlibname}

%description -n %{libname}
KSBA is a library designed to build software based on the X.509 and CMS
protocols.

%package -n %{devname}
Summary:	Development files for %{name} package
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains files needed to develop applications using %{name}.

%check
cd _OMV_rpm_build
%make_build check

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README THANKS TODO
%{_bindir}/ksba-config
%{_datadir}/aclocal/*
%{_includedir}/*.h
%doc %{_infodir}/*.info*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
