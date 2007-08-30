%define module	DBD-Multi
%define name	perl-%{module}
%define version	0.12
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Manage Multiple Data Sources with Failover and Load Balancing
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/DBD/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(DBD::File)
Buildrequires:	perl(DBD::SQLite)
Buildrequires:	perl(Class::Accessor::Fast)
Buildrequires:	perl(Sys::SigAction)
Buildrequires:	perl(Test::Pod)
Buildrequires:	perl(Test::Pod::Coverage)
Buildrequires:	perl(Test::Exception)
BuildArch:	noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/DBD
%_mandir/man3*/*

