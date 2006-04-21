#
# Conditional build:
%bcond_with	java # Java bindings
%bcond_without	ruby # Ruby bindings
%bcond_without	static_libs # don't build static libraries
#
Summary:	Full-text search system
Summary(pl):	Pe³notekstowy system wyszukiwawczy
Name:		hyperestraier
Version:	1.2.2
Release:	0.2
License:	LGPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/hyperestraier/%{name}-%{version}.tar.gz
# Source0-md5:	217cd4569d431972b2f9d75ac35239f1
Source1:	%{name}.sh
Patch0:		%{name}-am_ac.patch
URL:		http://hyperestraier.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	qdbm-devel >= 1.8.48-0.3
%{?with_java:BuildRequires:	jdk}
%{?with_ruby:BuildRequires:	ruby-devel}
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
 - Phrase search, regular expressions, attribute search, and
   similarity search
 - Multilingualism with Unicode
 - Independent of file format and repository
 - Simple and powerful API
 - Supporting P2P architecture

%description -l pl
Hyper Estraier to system wyszukiwania pe³notekstowego. Pozwala
przeszukiwaæ wiele dokumentów, aby odnale¼æ dokumenty zawieraj±ce
podane s³owa. W przypadku uruchomienia na stronie WWW, mo¿e byæ
przydatny jako w³asna wyszukiwarka stron we w³asnym serwisie. Jest
przydatny tak¿e do przeszukiwania skrzynek pocztowych i serwerów
plików.

Charakterystyka Hyper Estraiera:
 - du¿a wydajno¶æ przeszukiwania
 - du¿a skalowalno¶æ dokumentów docelowych
 - doskona³y wspó³czynnik odwo³añ przy u¿yciu metody N-gramowej
 - wysoka precyzja przy u¿yciu hybrydowego mechanizmu N-gramowego i
   analizatora morfologicznego
 - wyszukiwanie fraz, wyra¿eñ regularnych, atrybutów oraz podobieñst
 - wielojêzyczno¶æ z Unicode
 - niezale¿no¶æ od formatu plików i repozytorium
 - proste i potê¿ne API
 - obs³uga architektury P2P

%package libs
Summary:	hyperestraier libraries
Summary(pl):	Biblioteki hyperestraiera
Group:		Libraries

%description libs
hyperestraier libraries - full-text search system.

%description libs -l pl
Biblioteki hyperestraiera - pe³notekstowego systemu wyszukiwawczego.

%package devel
Summary:	Header files for hyperestraier library
Summary(pl):	Pliki nag³ówkowe biblioteki hyperestraier
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for hyperestraier
library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki hyperestraier.

%package static
Summary:	Static hyperestraier library
Summary(pl):	Statyczna biblioteka hyperestraier
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hyperestraier library.

%description static -l pl
Statyczna biblioteka hyperestraier.

%package javanative
Summary:	Java native bindings
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description javanative
Java native bindings.

%package javapure
Summary:	Java pure bindings
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description javapure
Java pure bindings.

%package rubynative
Summary:	Ruby native bindings
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%ruby_ver_requires_eq

%description rubynative
Ruby native bindings.

%package rubypure
Summary:	Ruby pure bindings
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%ruby_ver_requires_eq

%description rubypure
Ruby pure bindings.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%if %{with java}
cd javanative
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
cd -

cd javapure
%{__aclocal}
%{__autoconf}
#{__automake}
%configure
%{__make}
cd -
%endif

%if %{with ruby}
cd rubynative
%{__aclocal}
%{__autoconf}
%configure
%{__make}
cd -

cd rubypure
%{__aclocal}
%{__autoconf}
%configure
%{__make}
cd -
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with java}
%{__make} -C javanative install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C javapure install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with ruby}
%{__make} -C rubynative install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C rubypure install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}/{COPYING,ChangeLog,THANKS,doc}
install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS hyperestraier.sh
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
%attr(755,root,root) %{_libexecdir}/*.cgi
%attr(755,root,root) %{_libexecdir}/*.fcgi
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
# config templates - don't add to %%config, don't move it to /etc
%{_datadir}/%{name}/estseek.conf
%{_datadir}/%{name}/estseek.tmpl
%{_datadir}/%{name}/estseek.top
%{_datadir}/%{name}/estresult.dtd
%{_datadir}/%{name}/estraier.idl
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
%lang(ja) %{_datadir}/%{name}/locale/ja/estseek.tmpl
%lang(ja) %{_datadir}/%{name}/locale/ja/estseek.top

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/estconfig
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files javanative
%defattr(644,root,root,755)
%{_libdir}/estraier.jar

%files javapure
%defattr(644,root,root,755)
%{_libdir}/estraierpure.jar

%files rubynative
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/estcmd.rb
%attr(755,root,root) %{ruby_sitearchdir}/estraier.so

%files rubypure
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/estcall.rb
%{ruby_sitelibdir}/estraierpure.rb
