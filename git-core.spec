Summary:	The stupid content tracker
Summary(pl):	Prymitywne narzêdzie do ¶ledzenia tre¶ci
Name:		git-core
Version:	1.4.2.2
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
# Source0-md5:	9c8577e2e43fa08d68590928a4112547
URL:		http://git.or.cz/
BuildRequires:	asciidoc
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	xmlto
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"git" can mean anything, depending on your mood.

 - random three-letter combination that is pronounceable, and not
   actually used by any common UNIX command. The fact that it is a
   mispronunciation of "get" may or may not be relevant.
 - stupid. contemptible and despicable. simple. Take your pick from the
   dictionary of slang.
 - "global information tracker": you're in a good mood, and it actually
   works for you. Angels sing, and a light suddenly fills the room.
 - "goddamn idiotic truckload of sh*t": when it breaks

This is a stupid (but extremely fast) directory content manager. It
doesn't do a whole lot, but what it 'does' do is track directory
contents efficiently.

%description -l pl
"git" mo¿e oznaczaæ cokolwiek, w zale¿no¶ci od nastroju.

- losow± kombinacjê trzech liter, która jest wymawialna i w³a¶ciwie
  nie u¿ywana przez ¿adne popularne polecenie uniksowe. Fakt, ¿e jest to
  b³êdna pisownia s³owa "get" mo¿e mieæ lub nie mieæ znaczenia.
- g³upi, pogardliwy, prosty. Mo¿na wybraæ ze s³ownika slangu.
- "global information tracker" (narzêdzie do globalnego ¶ledzenia
  informacji) - je¶li jeste¶my w dobrym nastroju i git akurat dzia³a.
  Anio³y ¶piewaj±, a ¶wiat³o niespodziewanie wype³nia pokój.
- "goddamn idiotic truckload of sh*t" (przeklêty idiotyczny ³adunek
  g*) - kiedy siê zepsuje.

Jest to prymitywny (ale bardzo szybki) zarz±dca tre¶ci s³ownikowej.
Nie robi wiele, ale to, co "robi", to wydajne ¶ledzenie zawarto¶ci
katalogu.

%package devel
Summary:	Header files for git-core
Summary(pl):	Pliki nag³ówkowe dla git-core
Group:		Development/Libraries

%description devel
Header files for git-core.

%description devel
Pliki nag³ówkowe dla git-core.

%prep
%setup -q -n git-%{version}

%build
%{__make} \
	prefix=%{_prefix} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C Documentation

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}/xdiff

%{__make} install \
	prefix=%{_prefix} \
	CFLAGS="%{rpmcflags}" \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C Documentation install \
	prefix=%{_prefix} \
	mandir=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install xdiff/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xdiff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Documentation/*.html Documentation/howto Documentation/technical
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
