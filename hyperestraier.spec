#
# Conditional build:
%bcond_without	fcgi		# build estseek.fcgi
%bcond_without	java		# Java bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	static_libs	# don't build static libraries
#
%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine with_java
%endif
Summary:	Full-text search system
Summary(pl.UTF-8):	Pełnotekstowy system wyszukiwawczy
Name:		hyperestraier
Version:	1.4.13
Release:	7
License:	LGPL v2.1+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/hyperestraier/%{name}-%{version}.tar.gz
# Source0-md5:	847aefb9e23266545280378d797f3981
Source1:	%{name}.sh
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-ruby1.9.patch
Patch2:		ruby-vendor.patch
URL:		http://hyperestraier.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_fcgi:BuildRequires:	fcgi-devel}
%{?with_java:BuildRequires:	jdk}
%{?with_java:BuildRequires:	jpackage-utils}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qdbm-devel >= 1.8.75
%{?with_java:BuildRequires:	rpmbuild(macros) >= 1.300}
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Hyper Estraier is a full-text search system. You can search lots of
documents for some documents including specified words. If you run a
web site, it is useful as your own search engine for pages in your
site. Also, it is useful as search utilities of mail boxes and file
servers.

The characteristic of Hyper Estraier is the following:
 - High performance of search
 - High scalability of target documents
 - Perfect recall ratio by N-gram method
 - High precision by hybrid mechanism of N-gram and morphological
   analyzer
 - Phrase search, regular expressions, attribute search, and similarity
   search
 - Multilingualism with Unicode
 - Independent of file format and repository
 - Simple and powerful API
 - Supporting P2P architecture

%description -l pl.UTF-8
Hyper Estraier to system wyszukiwania pełnotekstowego. Pozwala
przeszukiwać wiele dokumentów, aby odnaleźć dokumenty zawierające
podane słowa. W przypadku uruchomienia na stronie WWW, może być
przydatny jako własna wyszukiwarka stron we własnym serwisie. Jest
przydatny także do przeszukiwania skrzynek pocztowych i serwerów
plików.

Charakterystyka Hyper Estraiera:
 - duża wydajność przeszukiwania
 - duża skalowalność dokumentów docelowych
 - doskonały współczynnik odwołań przy użyciu metody N-gramowej
 - wysoka precyzja przy użyciu hybrydowego mechanizmu N-gramowego i
   analizatora morfologicznego
 - wyszukiwanie fraz, wyrażeń regularnych, atrybutów oraz podobieńst
 - wielojęzyczność z Unicode
 - niezależność od formatu plików i repozytorium
 - proste i potężne API
 - obsługa architektury P2P

%package libs
Summary:	hyperestraier libraries
Summary(pl.UTF-8):	Biblioteki hyperestraiera
Group:		Libraries

%description libs
hyperestraier libraries - full-text search system.

%description libs -l pl.UTF-8
Biblioteki hyperestraiera - pełnotekstowego systemu wyszukiwawczego.

%package devel
Summary:	Header files for hyperestraier library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hyperestraier
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for hyperestraier
library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki hyperestraier.

%package static
Summary:	Static hyperestraier library
Summary(pl.UTF-8):	Statyczna biblioteka hyperestraier
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hyperestraier library.

%description static -l pl.UTF-8
Statyczna biblioteka hyperestraier.

%package javanative
Summary:	Java native bindings for hyperestraier
Summary(pl.UTF-8):	Wiązania natywne Javy do hyperestraiera
Group:		Libraries/Java
Requires:	%{name}-devel = %{version}-%{release}

%description javanative
Java native bindings for hyperestraier.

%description javanative -l pl.UTF-8
Wiązania natywne Javy do hyperestraiera.

%package javapure
Summary:	Java pure bindings for hyperestraier
Summary(pl.UTF-8):	Wiązania Javy do hyperestraiera w czystej Javie
License:	BSD-style
Group:		Libraries/Java

%description javapure
Java pure bindings for hyperestraier.

%description javapure -l pl.UTF-8
Wiązania Javy do hyperestraiera w czystej Javie.

%package rubynative
Summary:	Ruby native bindings for hyperestraier
Summary(pl.UTF-8):	Wiązania natywne języka Ruby do hyperestraiera
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}

%description rubynative
Ruby native bindings for hyperestraier.

%description rubynative -l pl.UTF-8
Wiązania natywne języka Ruby do hyperestraiera.

%package rubypure
Summary:	Ruby pure bindings
Summary(pl.UTF-8):	Wiązania języka Ruby do hyperestraiera w czystym Rubym
License:	BSD-style
Group:		Development/Libraries

%description rubypure
Ruby pure bindings for hyperestraier.

%description rubypure -l pl.UTF-8
Wiązania języka Ruby do hyperestraiera w czystym Rubym.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-fcgi%{!?with_fcgi:=no} \
	--enable-static%{!?with_static_libs:=no}
%{__make}

%if %{with java}
export JAVA_HOME="%{java_home}"
cd javanative
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}
cd ../javapure
%{__aclocal}
%{__autoconf}
%configure
%{__make}
cd ..
%endif

%if %{with ruby}
cd rubynative
%{__aclocal}
%{__autoconf}
%configure
%{__make}
cd ../rubypure
%{__aclocal}
%{__autoconf}
%configure
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with java}
%{__make} -C javanative install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libjestraier.la

%{__make} -C javapure install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with ruby}
%{__make} -C rubynative install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C rubypure install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	javanative -p /sbin/ldconfig
%postun	javanative -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS hyperestraier.sh
%attr(755,root,root) %{_bindir}/estbutler
%attr(755,root,root) %{_bindir}/estcall
%attr(755,root,root) %{_bindir}/estcmd
%attr(755,root,root) %{_bindir}/estload
%attr(755,root,root) %{_bindir}/estmaster
%attr(755,root,root) %{_bindir}/estmttest
%attr(755,root,root) %{_bindir}/estwaver
%attr(755,root,root) %{_bindir}/estwolefind
# don't move cgi binaries to /usr/lib/cgi-bin - write your own wrapper
# (shell script) instead, utilize SCRIPT_NAME env. var. and put into
# your cgi-bin directory
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/est*.cgi
%{?with_fcgi:%attr(755,root,root) %{_libexecdir}/est*.fcgi}
%{_mandir}/man1/estcall.1*
%{_mandir}/man1/estcmd.1*
%{_mandir}/man1/estconfig.1*
%{_mandir}/man1/estmaster.1*
%{_mandir}/man1/estwaver.1*
%dir %{_datadir}/%{name}
# config templates - don't add to %%config, don't move it to /etc
%{_datadir}/%{name}/estseek.conf
%{_datadir}/%{name}/estseek.tmpl
%{_datadir}/%{name}/estseek.top
%{_datadir}/%{name}/estseek.help
%{_datadir}/%{name}/estresult.dtd
%{_datadir}/%{name}/estraier.idl
%{_datadir}/%{name}/estfraud.conf
%{_datadir}/%{name}/estproxy.conf
%{_datadir}/%{name}/estscout.conf
%{_datadir}/%{name}/estsupt.conf
%dir %{_datadir}/%{name}/filter
%{_datadir}/%{name}/filter/estfxmantotxt
%{_datadir}/%{name}/filter/estfxmsotohtml
%{_datadir}/%{name}/filter/estfxasis
%{_datadir}/%{name}/filter/estfxpdftohtml
%{_datadir}/%{name}/filter/estwnetxpnd
%{_datadir}/%{name}/filter/estfxxdwtotxt
%dir %{_datadir}/%{name}/increm
%{_datadir}/%{name}/increm/estseek-frame.html
%{_datadir}/%{name}/increm/estseek-form.html
%dir %{_datadir}/%{name}/locale
%lang(ja) %dir  %{_datadir}/%{name}/locale/ja
%lang(ja) %{_datadir}/%{name}/locale/ja/estseek.conf
%lang(ja) %{_datadir}/%{name}/locale/ja/estseek.help
%lang(ja) %{_datadir}/%{name}/locale/ja/estseek.tmpl
%lang(ja) %{_datadir}/%{name}/locale/ja/estseek.top

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libestraier.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libestraier.so.8

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/estconfig
%attr(755,root,root) %{_libdir}/libestraier.so
%{_libdir}/libestraier.la
%{_includedir}/estmtdb.h
%{_includedir}/estnode.h
%{_includedir}/estraier.h
%{_pkgconfigdir}/hyperestraier.pc
%{_mandir}/man3/estnode.3*
%{_mandir}/man3/estraier.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libestraier.a
%endif

%if %{with java}
%files javanative
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjestraier.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjestraier.so.1
%attr(755,root,root) %{_libdir}/libjestraier.so
%{_libdir}/estraier.jar

%files javapure
%defattr(644,root,root,755)
%{_libdir}/estraierpure.jar
%endif

%if %{with ruby}
%files rubynative
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/estcmd.rb
%attr(755,root,root) %{ruby_vendorarchdir}/estraier.so

%files rubypure
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/estcall.rb
%{ruby_vendorlibdir}/estraierpure.rb
%endif
