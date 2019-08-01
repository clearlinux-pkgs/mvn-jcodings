#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jcodings
Version  : 1.0.13
Release  : 1
URL      : https://github.com/jruby/jcodings/archive/jcodings-1.0.13.tar.gz
Source0  : https://github.com/jruby/jcodings/archive/jcodings-1.0.13.tar.gz
Source1  : https://repo1.maven.org/maven2/org/jruby/jcodings/jcodings/1.0.13/jcodings-1.0.13.jar
Source2  : https://repo1.maven.org/maven2/org/jruby/jcodings/jcodings/1.0.13/jcodings-1.0.13.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-jcodings-data = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
jcodings
========
Java-based codings helper classes for Joni and JRuby
## License

%package data
Summary: data components for the mvn-jcodings package.
Group: Data

%description data
data components for the mvn-jcodings package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jruby/jcodings/jcodings/1.0.13
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/jruby/jcodings/jcodings/1.0.13/jcodings-1.0.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jruby/jcodings/jcodings/1.0.13
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/jruby/jcodings/jcodings/1.0.13/jcodings-1.0.13.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/jruby/jcodings/jcodings/1.0.13/jcodings-1.0.13.jar
/usr/share/java/.m2/repository/org/jruby/jcodings/jcodings/1.0.13/jcodings-1.0.13.pom
