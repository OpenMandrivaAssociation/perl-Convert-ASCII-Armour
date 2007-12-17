Name:           perl-Convert-ASCII-Armour
Version:        1.4
Release:        %mkrel 4
License:        Artistic

%define realname        Convert-ASCII-Armour
Group:          Development/Perl
Summary:        Convert binary octets into ASCII armoured messages
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/%{realname}-%{version}.tar.bz2
Url:            http://www.cpan.org
Prefix:         %{_prefix}
BuildRequires:  perl-Compress-Zlib
Requires:       perl
BuildArch:      noarch

%description 
This module converts hashes of binary octets into ASCII
messages suitable for transfer over 6-bit clean transport
channels. The encoded ASCII resembles PGP's armoured
messages, but are in no way compatible with PGP.

%prep
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/*/*

