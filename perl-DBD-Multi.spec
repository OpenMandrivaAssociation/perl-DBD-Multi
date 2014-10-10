%define upstream_name	 DBD-Multi
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.18
Release:	2

Summary:	Manage Multiple Data Sources with Failover and Load Balancing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBD/DBD-Multi-0.18.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::File)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Sys::SigAction)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Exception)

BuildArch:	noarch

%description
This software manages multiple database connections for failovers and also
simple load balancing. It acts as a proxy between your code and your database
connections, transparently choosing a connection for each query, based on your
preferences and present availability of the DB server.

This module is intended for read-only operations (where some other application
is being used to handle replication).

This software does not prevent write operations from being executed. This is
left up to the user. See "SUGGESTED USES" below for ideas.

The interface is nearly the same as other DBI drivers with one notable
exception.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/DBD
%{_mandir}/man3/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 681353
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 587610
- new version

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 554300
- update to 0.15

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 403093
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.14-3mdv2009.0
+ Revision: 256563
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2008.1
+ Revision: 178293
- update to new version 0.14

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2008.1
+ Revision: 173870
- update to new version 0.13

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.0
+ Revision: 75219
- update to new version 0.12

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.0
+ Revision: 65372
- update to new version 0.11

* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
+ Revision: 49009
- import perl-DBD-Multi


* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
- first mdv release 

