#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-ContentType
Summary:	Email::MIME::ContentType - parse a MIME Content-Type header
Summary(pl.UTF-8):	Email::MIME::ContentType - analiza nagłówka MIME Content-Type
Name:		perl-Email-MIME-ContentType
Version:	1.014
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9189eae13bbb405f4ef9d254f99aef70
URL:		http://search.cpan.org/dist/Email-MIME-ContentType/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is responsible for parsing email content type headers
according to section 5.1 of RFC 2045. It returns a hash as above,
with entries for the discrete type, the composite type, and a hash
of attributes.

%description -l pl.UTF-8
Ten moduł odpowiada za analizę nagłówków listów dotyczących rodzaju
zawartości zgodnie z rozdziałem 5.1 RFC 2045. Zwraca hasza z wpisami
dla typu dyskretnego, typu złożonego i hasza atrybutów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/MIME/*.pm
%{_mandir}/man3/*
