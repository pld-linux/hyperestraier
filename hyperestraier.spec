Summary:	Full-text search system
Summary(pl):	Pe�notekstowy system wyszukiwawczy
Name:		hyperestraier
Version:	1.2.1
Release:	1	
License:	LGPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/hyperestraier/%{name}-%{version}.tar.gz
# Source0-md5:	91e2c859510a9e30fad8b49f6affe6f1
Source1:	%{name}.sh
URL:		http://hyperestraier.sourceforge.net/
BuildRequires:	qdbm-devel >= 1.8.48-0.3
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
Hyper Estraier to system wyszukiwania pe�notekstowego. Pozwala
przeszukiwa� wiele dokument�w, aby odnale�� dokumenty zawieraj�ce
podane s�owa. W przypadku uruchomienia na stronie WWW, mo�e by�
przydatny jako w�asna wyszukiwarka stron we w�asnym serwisie. Jest
przydatny tak�e do przeszukiwania skrzynek pocztowych i serwer�w
plik�w.

Charakterystyka Hyper Estraiera:
 - du�a wydajno�� przeszukiwania
 - du�a skalowalno�� dokument�w docelowych
 - doskona�y wsp�czynnik odwo�a� przy u�yciu metody N-gramowej
 - wysoka precyzja przy u�yciu hybrydowego mechanizmu N-gramowego i
   analizatora morfologicznego
 - wyszukiwanie fraz, wyra�e� regularnych, atrybut�w oraz podobie�st
 - wieloj�zyczno�� z Unicode
 - niezale�no�� od formatu plik�w i repozytorium
 - proste i pot�ne API
 - obs�uga architektury P2P

%package libs
Summary:	hyperestraier libraries
Summary(pl):	Biblioteki hyperestraiera
Group:		Libraries

%description libs
hyperestraier libraries - full-text search system.

%description libs -l pl
Biblioteki hyperestraiera - pe�notekstowego systemu wyszukiwawczego.

%package devel
Summary:	Header files for hyperestraier library
Summary(pl):	Pliki nag��wkowe biblioteki hyperestraier
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for hyperestraier
library.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe biblioteki hyperestraier.

%package static
Summary:	Static hyperestraier library
Summary(pl):	Statyczna biblioteka hyperestraier
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hyperestraier library.

%description static -l pl
Statyczna biblioteka hyperestraier.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}/{COPYING,ChangeLog,THANKS,doc}
install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS hyperestraier.sh
%attr(755,root,root) %{_bindir}/*
# don't move cgi binaries to /usr/lib/cgi-bin - write your own wrapper
# (shell script) instead, utilize SCRIPT_NAME env. var. and put into
# your cgi-bin directory
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/*.cgi
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
