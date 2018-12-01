%define upstream_name    Sereal-Decoder
%define upstream_version 4.005

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Getting the most out of the Perl-Sereal implementation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
# Source0:    http://www.cpan.org/modules/by-module/Sereal/%{upstream_name}-%{upstream_version}.tar.gz
Source0:    https://cpan.metacpan.org/authors/id/Y/YV/YVES/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker) >= 7.0.0
BuildRequires: perl(ExtUtils::ParseXS) >= 2.210.0
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(Test::Warn)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel
%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

# (tv) // build is broken:
make

%check
%__make test

%install
%make_install

%files
%doc Changes INSTALL META.json META.yml MYMETA.yml
%{_mandir}/man3/*
%perl_vendorarch/*
