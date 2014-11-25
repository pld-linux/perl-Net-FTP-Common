#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)

%define		pdir	Net
%define		pnam	FTP-Common
%include	/usr/lib/rpm/macros.perl
Summary:	Net::FTP::Common - simplify common usages of Net::FTP
Summary(pl.UTF-8):	Net::FTP::Common - uproszczenie popularnych sposobów użycia Net::FTP
Name:		perl-Net-FTP-Common
Version:	7.0.d
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15b1b719b5ac26a0122775c2e68c7d5c
URL:		http://search.cpan.org/dist/Net-FTP-Common/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Net::FTP) >= 1
%endif
# for Net::FTP and directory
Requires:	perl-libnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to make the common uses of Net::FTP a
one-line, no-argument affair. In other words, you have 100%
programming with Net::FTP. With Net::FTP::Common you will have 95%
configuration and 5% programming.

%description -l pl.UTF-8
Ten moduł ma uczynić popularne sposoby użycia Net::FTP
jednolinijkowymi wywołaniami bez argumentów. Innymi słowy, przy użyciu
Net::FTP mamy 100% programowania. Przy użyciu Net::FTP::Common mamy
95% konfiguracji i 5% programowania.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/TestConfig.pm
%{perl_vendorlib}/%{pdir}/FTP/Common.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
