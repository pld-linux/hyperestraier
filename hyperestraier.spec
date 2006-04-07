Summary:	Full-text search system
Summary(pl):	Pe³notekstowy system wyszukiwawczy
Name:		hyperestraier
Version:	1.1.6
Release:	0.1
License:	LGPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/hyperestraier/%{name}-%{version}.tar.gz
# Source0-md5:	a688ebda299a033f61321f0d70adad84
URL:		http://hyperestraier.sourceforge.net/
BuildRequires:	qdbm-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Hyper Estraier is a full-text search system. You can search lots of
documents for some documents including specified words. If you run a
web site, it is useful as your own search engine for pages in your
site. Also, it is useful as search utilities of mail boxes and file
servers.

The characteristic of Hyper Estraier is the following.

     - High performance of search
     - High scalability of target documents
     - Perfect recall ratio by N-gram method
     - High precision by hybrid mechanism of N-gram and morphological
     - analyzer
     - Phrase search, regular expressions, attribute search, and
     - similarity search
     - Multilingualism with Unicode
     - Independent of file format and repository
     - Simple and powerful API
     - Supporting P2P architecture

#%%description -l pl

%package libs
Summary:	hyperestraier
Summary(pl):	hyperestraier
Group:		Libraries

%description libs
hyperestraier libraries - full-text search system.

%description libs -l pl
Biblioteki hyperestraier - pe³notekstowego systemu wyszukiwawczego.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/*
# don't move it to /usr/lib/cgi-bin - write your wrapper (sh script),
# utilize SCRIPT_NAME env. var. and put into your cgi-bin directory
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
