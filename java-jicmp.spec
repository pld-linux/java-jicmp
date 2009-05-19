#
%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif

%define		pkg	jicmp

%include	/usr/lib/rpm/macros.java
Summary:	Java interface to ICMP (ping)
Name:		java-%{pkg}
Version:	1.0.10
Release:	1
License:	GPL
Group:		Libraries/Java
Source0:	http://dl.sourceforge.net/opennms/%{pkg}-%{version}.tar.gz
# Source0-md5:	6473716859058697ae78a7d70c6aebbf
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JICMP is a Java interface to the ICMP protocol (ping), originally
written as a part of OpenNMS.

%prep
%setup -q -n %{pkg}-%{version}

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
