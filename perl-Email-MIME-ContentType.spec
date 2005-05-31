#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-ContentType
Summary:	Email::MIME::ContentType - parse a MIME Content-Type header
Summary(pl):	Email::MIME::ContentType - przetwarzanie nag��wka MIME Content-Type
Name:		perl-Email-MIME-ContentType
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1aa682d2841f5d568416772bbaede1c9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is responsible for parsing email content type headers
according to section 5.1 of RFC 2045. It returns a hash as above,
with entries for the discrete type, the composite type, and a hash
of attributes.

%description -l pl
Ten modu� odpowiada za przetwarzanie nag��wk�w list�w dotycz�cych
rodzaju zawarto�ci zgodnie z rozdzia�em 5.1 RFC 2045. Zwraca hasza
z wpisami dla typu dyskretnego, typu z�o�onego i hasza atrybut�w.

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
