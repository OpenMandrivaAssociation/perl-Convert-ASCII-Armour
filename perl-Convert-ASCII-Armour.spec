%define realname Convert-ASCII-Armour


Name:		perl-%{realname}
Version:	1.4
Release:	14
Summary:	Convert binary octets into ASCII armoured messages
License:	Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/%{realname}-%{version}.tar.bz2
BuildRequires:	perl(Compress::Zlib)  
BuildRequires:	perl-devel
BuildArch:		noarch

%description 
This module converts hashes of binary octets into ASCII
messages suitable for transfer over 6-bit clean transport
channels. The encoded ASCII resembles PGP's armoured
messages, but are in no way compatible with PGP.

%prep
%setup -q -n %{realname}-%{version}

%build
CFLAGS="%{optflags}" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4-11mdv2012.0
+ Revision: 765108
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4-10
+ Revision: 763565
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-9
+ Revision: 676516
- rebuild

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.4-8
+ Revision: 653398
- rebuild for updated spec-helper

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 1.4-7mdv2011.0
+ Revision: 432208
- fix BR
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 241192
- rebuild
- fix no-buildroot-tag
- kill (multiple!) definitions of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-4mdv2008.0
+ Revision: 86212
- rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:53:08 (58422)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:51:25 (58419)
Import perl-Convert-ASCII-Armour

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.4-2mdk
- rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.4-1mdk
- New package

