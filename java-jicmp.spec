
%define		srcname	jicmp

%include	/usr/lib/rpm/macros.java
Summary:	Java interface to ICMP (ping)
Name:		java-%{srcname}
Version:	1.0.10
Release:	1
License:	GPL
Group:		Libraries/Java
Source0:	http://downloads.sourceforge.net/opennms/%{srcname}-%{version}.tar.gz
# Source0-md5:	6473716859058697ae78a7d70c6aebbf
BuildRequires:	jdk
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JICMP is a Java interface to the ICMP protocol (ping), originally
written as a part of OpenNMS.

%prep
%setup -q -n %{srcname}-%{version}

%build
export JAVA_HOME=%{java_home}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjicmp*
%{_javadir}/*.jar
