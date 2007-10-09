#
# Conditional build:
%bcond_without	tests	# don't perform make test
#
%include	/usr/lib/rpm/macros.perl
Summary:	The stupid content tracker
Summary(pl.UTF-8):	Prymitywne narzędzie do śledzenia treści
Name:		git-core
Version:	1.5.3.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
# Source0-md5:	b35fd5abba0e8655733c8e8c470f39cf
Source1:	%{name}-gitweb.conf
Source2:	%{name}-gitweb-httpd.conf
URL:		http://git.or.cz/
BuildRequires:	asciidoc >= 7.1.2-3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-Error
BuildRequires:	perl-base
%{?with_tests:BuildRequires:	pdksh >= 5.2.14-46}
BuildRequires:	python
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.264
BuildRequires:	xmlto
BuildRequires:	zlib-devel
Requires:	coreutils
Requires:	curl
Requires:	diffutils
Requires:	findutils
Requires:	grep
Requires:	openssh-clients
Requires:	perl-Error
Requires:	rcs
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webapp		gitweb
%define		webappdir	%{_sysconfdir}/webapps/%{webapp}
%define		appdir		%{_datadir}/%{webapp}
%define		cgibindir	%{_prefix}/lib/cgi-bin

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

%description -l pl.UTF-8
"git" może oznaczać cokolwiek, w zależności od nastroju.

- losową kombinację trzech liter, która jest wymawialna i
  właściwie nie używana przez żadne popularne polecenie uniksowe.
  Fakt, że jest to błędna pisownia słowa "get" może mieć lub nie
  mieć znaczenia.
- głupi, pogardliwy, prosty. Można wybrać ze słownika slangu.
- "global information tracker" (narzędzie do globalnego śledzenia
  informacji) - jeśli jesteśmy w dobrym nastroju i git akurat działa.
  Anioły śpiewają, a światło niespodziewanie wypełnia pokój.
- "goddamn idiotic truckload of sh*t" (przeklęty idiotyczny ładunek
  g*) - kiedy się zepsuje.

Jest to prymitywny (ale bardzo szybki) zarządca treści słownikowej.
Nie robi wiele, ale to, co "robi", to wydajne śledzenie zawartości
katalogu.

%package devel
Summary:	Header files for git-core
Summary(pl.UTF-8):	Pliki nagłówkowe dla git-core
Group:		Development/Libraries

%description devel
Header files for git-core.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla git-core.

%package gitk
Summary:	Tcl/Tk interface to the Git version control system
Summary(pl.UTF-8):	Napisany w Tcl/Tk interfejs do systemu kontroli wersji Git
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	tk

%description gitk
Displays changes in a repository or a selected set of commits. This
includes visualizing the commit graph, showing information related to
each commit, and the files in the trees of each revision.

Historically, gitk was the first repository browser. It's written in
Tcl/Tk and started off in a separate repository but was later merged
into the main git repository.

%description gitk -l pl.UTF-8
Wyświetla zmiany w repozytorium lub wybranym zbiorze commitów.
Oznacza to wizualizację grafu commitów, wyświetlanie informacji
związanych z każdym z commitów oraz listę plików dla każdej
rewizji.

Z punktu widzenia historii, gitk był pierwszą przeglądarką
repozytorium git. Napisany jest w Tcl/Tk i początkowo był rozwijany
w osobnym repozytorium, ale z czasem został włączony do głównego
repozytorium gita.

%package gitweb
Summary:	Web frontend to git
Summary(pl.UTF-8):	Webowy frontend do git
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	webapps

%description gitweb
This package provides a web interface for browsing git repositories.

%description gitweb -l pl.UTF-8
Pakiet ten dostarcza interfejs WWW do przeglądania repozytoriów gita.

%package gitview
Summary:	A GTK based repository browser for git
Summary(pl.UTF-8):	Oparta na GTK przeglądarka repozytorium gita
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
#Requires:	pytongowe mambo dżambo

%description gitview
A GTK based repository browser for git.

%description gitview -l pl.UTF-8
Oparta na GTK przeglądarka repozytorium gita.

%package -n bash-completion-git
Summary:	bash-completion for git
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla gita
Group:		Applications/Shell
Requires:	bash-completion

%description -n bash-completion-git
This package provides bash-completion for git.

%description -n bash-completion-git -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla gita.

%package -n perl-Git
Summary:	Perl interface to the Git version control system
Summary(pl.UTF-8):	Perlowy interfejs do systemu kontroli wersji Git
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	perl-git-core

%description -n perl-Git
This module provides Perl scripts easy way to interface the Git
version control system. The modules have an easy and well-tested way
to call arbitrary Git commands; in the future, the interface will also
provide specialized methods for doing easily operations which are not
totally trivial to do over the generic command interface.

%description -n perl-Git -l pl.UTF-8
Ten moduł umożliwia skryptom Perla współpracę z systemem kontroli
wersji Git. W łatwy i dobrze przetestowany sposób pozwala
wywoływać dowolne polecenia Gita; w przyszłości interfejs
udostępni także specjalne metody do łatwego wykonywania operacji
nietrywialnych do wykonania przy użyciu ogólnego interfejsu
poleceń.

%package -n vim-syntax-gitcommit
Summary:	Vim syntax: gitcommit
Summary(pl.UTF-8):	Składnia dla Vima: gitcommit
Group:		Applications/Editors/Vim
# for _vimdatadir existence
Requires:       vim >= 4:6.3.058-3

%description -n vim-syntax-gitcommit
This plugin provides syntax highlighting for git's commit messages.

%description -n vim-syntax-gitcommit -l pl.UTF-8
Ta wtyczka dostarcza podświetlanie składni dla treści commitów gita.

%prep
%setup -q -n git-%{version}

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-openssl

%{__make} \
	INSTALLDIRS=vendor \
	GITWEB_CONFIG="%{webappdir}/gitweb.conf" \
	GITWEB_PROJECTROOT="/var/lib/git" \
	GITWEB_CSS="/gitweb/gitweb.css" \
	GITWEB_LOGO="/gitweb/git-logo.png" \
	GITWEB_FAVICON="/gitweb/git-favicon.png"

%{__make} -C Documentation

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name}/xdiff,%{_sharedstatedir}/git}
install -d $RPM_BUILD_ROOT{%{appdir},%{cgibindir},%{webappdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%{__make} install \
	INSTALLDIRS=vendor \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C Documentation install \
	DESTDIR=$RPM_BUILD_ROOT

# header files and lib
install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install xdiff/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xdiff
install libgit.a $RPM_BUILD_ROOT%{_libdir}

# bash completion
install contrib/completion/git-completion.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

# vim syntax
install contrib/vim/syntax/gitcommit.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax

# gitweb
install gitweb/*.css gitweb/*.png $RPM_BUILD_ROOT%{appdir}
install gitweb/gitweb.cgi $RPM_BUILD_ROOT%{cgibindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{webappdir}/gitweb.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{webappdir}/apache.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{webappdir}/httpd.conf

# gitview
install contrib/gitview/gitview $RPM_BUILD_ROOT%{_bindir}

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Git/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin gitweb -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{webapp}

%triggerun gitweb -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{webapp}

%triggerin gitweb -- apache < 2.2.0, apache-base
%webapp_register httpd %{webapp}

%triggerun gitweb -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{webapp}

%files
%defattr(644,root,root,755)
%doc README Documentation/{[!g]*,g[!i]*,git,git[!k]*}.html Documentation/howto Documentation/technical contrib
%attr(755,root,root) %{_bindir}/git
%attr(755,root,root) %{_bindir}/git-*
%{_mandir}/man1/git-*.1*
%{_mandir}/man5/gitattributes.5*
%{_mandir}/man5/gitignore.5*
%{_mandir}/man5/gitmodules.5*
%{_mandir}/man7/git.7*
%{_datadir}/%{name}
%{_datadir}/git-gui
%{_sharedstatedir}/git

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a

%files gitk
%defattr(644,root,root,755)
%doc Documentation/gitk.html
%attr(755,root,root) %{_bindir}/gitk
%{_mandir}/man1/gitk.1*

%files gitweb
%defattr(644,root,root,755)
%doc gitweb/{README,INSTALL}
%dir %{webappdir}
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,http) %{webappdir}/gitweb.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/apache.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/httpd.conf
%attr(755,root,root) %{cgibindir}/gitweb.cgi
%{appdir}

%files gitview
%defattr(644,root,root,755)
%doc contrib/gitview/gitview.txt
%attr(755,root,root) %{_bindir}/gitview

%files -n bash-completion-git
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*

%files -n perl-Git
%defattr(644,root,root,755)
%{perl_vendorlib}/Git.pm
%{_mandir}/man3/Git.3pm*

%files -n vim-syntax-gitcommit
%defattr(644,root,root,755)
%doc contrib/vim/README
%{_datadir}/vim/vimfiles/syntax/*
