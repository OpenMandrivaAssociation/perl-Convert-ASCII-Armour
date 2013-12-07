%define realname Convert-ASCII-Armour

Summary:	Convert binary octets into ASCII armoured messages
Name:		perl-%{realname}
Version:	1.4
Release:	17
License:	Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)  
BuildArch:	noarch

%description 
This module converts hashes of binary octets into ASCII
messages suitable for transfer over 6-bit clean transport
channels. The encoded ASCII resembles PGP's armoured
messages, but are in no way compatible with PGP.

%prep
%setup -qn %{realname}-%{version}

%build
CFLAGS="%{optflags}" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

