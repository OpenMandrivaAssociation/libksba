%define major 8
%define libname %mklibname ksba %{major}
%define develname %mklibname ksba -d

Summary:        Library handling X.509 certificates and CMS data
Name:           libksba
Version:        1.2.0
Release:        5
License:        GPLv3
Group:          System/Libraries
URL:            http://www.gnupg.org/
Source0:        ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRequires:  libgpg-error-devel >= 1.2

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
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/ksba-config

%check
%make check

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README THANKS TODO
%{multiarch_bindir}/ksba-config
%{_bindir}/ksba-config
%{_datadir}/aclocal/*
%{_includedir}/*.h
%{_infodir}/*.info*
%{_libdir}/*.so


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2011.0
+ Revision: 661679
- multiarch fixes

* Tue Mar 01 2011 Lonyai Gergely <aleph@mandriva.org> 1.2.0-1
+ Revision: 641167
- 1.2.0

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 611875
- update to new version 1.1.0

* Mon Aug 16 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 570331
- New version 1.0.8
- update files list

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2mdv2010.1
+ Revision: 520875
- rebuilt for 2010.1

* Sun Jul 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.7-1mdv2010.0
+ Revision: 400299
- New version 1.0.7

* Tue Jan 13 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.5-1mdv2009.1
+ Revision: 329152
- New version 1.O.5

* Wed Jan 07 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.4-1mdv2009.1
+ Revision: 326823
- New version 1.0.4
- drop old conditionnals

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 222914
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 173706
- new version
- new devel library policy
- do not provide COPYING file
- make use of %%major in file list

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 150701
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jul 06 2007 Andreas Hasenack <andreas@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 49172
- updated to version 1.0.2
- updated license tag to GPLv3


* Thu Nov 16 2006 David Walluck <walluck@mandriva.org> 1.0.0-1mdv2007.0
+ Revision: 84690
- 1.0.0
- Import libksba

* Mon Jul 24 2006 Emmanuel Andry <eandry@mandriva.org> 0.9.15-1mdv2007.0
- updated to version 0.9.15
- %%mkrel

* Fri Dec 02 2005 Andreas Hasenack <andreas@mandriva.com> 0.9.13-1mdk
- updated to version 0.9.13
- dropping automake17 buildrequirement, seems to build fine with 1.9

* Tue Sep 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.11-2mdk
- rebuild

* Thu May 19 2005 Arnaud de Lorbeau <adelorbeau@mandriva.com> 0.9.11-1mdk
- 0.9.11

* Sat Apr 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.10-2mdk
- fix deps and conditional %%multiarch
- requires-on-release

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrakesoft.com> 0.9.10-1mdk
- New release 0.9.10

* Fri Aug 20 2004 Abel Cheung <deaddog@deaddog.org> 0.9.8-1mdk
- New version
- P1: Fix parallel build

* Fri May 21 2004 Abel Cheung <deaddog@deaddog.org> 0.9.6-1mdk
- New version
- Patch0: automake 1.8 compatibility

* Sat Jan 24 2004 Abel Cheung <deaddog@deaddog.org> 0.9.1-1mdk
- New version

* Wed Dec 10 2003 Abel Cheung <deaddog@deaddog.org> 0.9.0-1mdk
- New version
- Use official tar.gz instead, for proving legitimacy

