#
# Conditional build:
%bcond_without	tests		# don't perform make test
%bcond_with	tests_cvs	# perform tests which use CVS
%bcond_with	tests_svn	# perform tests which use subversion
%bcond_without	doc		# skip building/packaging docs/manuals (takes some time)

%include	/usr/lib/rpm/macros.perl
Summary:	Distributed version control system focused on speed, effectivity and usability
Summary(pl.UTF-8):	Rozproszony system śledzenia treści skupiony na szybkości, wydajności i użyteczności
Name:		git-core
Version:	1.7.10.1
Release:	1
License:	GPL v2
Group:		Development/Tools
# Source0:	http://www.kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
Source0:	http://git-core.googlecode.com/files/git-%{version}.tar.gz
# Source0-md5:	41da844a1b8cc2d92864381e2fdeb0e1
Source1:	%{name}-gitweb.conf
Source2:	%{name}-gitweb-httpd.conf
Source3:	%{name}-gitweb-lighttpd.conf
Source4:	%{name}.sysconfig
Source5:	%{name}.inet
Source6:	%{name}.init
Patch0:		%{name}-tests.patch
Patch1:		%{name}-key-bindings.patch
Patch2:		%{name}-sysconfdir.patch
URL:		http://git-scm.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-Error > 0.15
BuildRequires:	perl-base
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.264
BuildRequires:	tcl
BuildRequires:	zlib-devel
%if %{with doc}
BuildRequires:	asciidoc >= 7.1.2-3
BuildRequires:	docbook-dtd45-xml
BuildRequires:	xmlto
%endif
%if %{with tests}
%if %{with tests_cvs}
# tests failed sometimes when using nserver/cvsnt client so enforce pure cvs here
BuildRequires:	cvs-gnu-client < 1.13
BuildRequires:	cvs-gnu-client >= 1.12
%endif
Conflicts:	pdksh < 5.2.14-46
%endif
Requires:	coreutils
Requires:	diffutils
Requires:	findutils
Requires:	grep
Requires:	openssh-clients
Requires:	perl-Error
Requires:	perl-Git = %{version}-%{release}
Requires:	sed
Suggests:	git-core-cvs
Suggests:	git-core-svn
Suggests:	less
Suggests:	rsync
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# html docs have links to txt files
%define		_noautocompressdoc	*.txt

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

- losową kombinację trzech liter, która jest wymawialna i właściwie
  nie używana przez żadne popularne polecenie uniksowe. Fakt, że jest to
  błędna pisownia słowa "get" może mieć lub nie mieć znaczenia.
- głupi, pogardliwy, prosty. Można wybrać ze słownika slangu.
- "global information tracker" (narzędzie do globalnego śledzenia
  informacji) - jeśli jesteśmy w dobrym nastroju i git akurat działa.
  Anioły śpiewają, a światło niespodziewanie wypełnia pokój.
- "goddamn idiotic truckload of sh*t" (przeklęty idiotyczny ładunek
  g*) - kiedy się zepsuje.

Jest to prymitywny (ale bardzo szybki) zarządca treści słownikowej.
Nie robi wiele, ale to, co "robi", to wydajne śledzenie zawartości
katalogu.

%package doc
Summary:	Documentation for git-core
Summary(pl.UTF-8):	Dokumentacja do git-core
Group:		Documentation

%description doc
Documentation for git-core.

%description doc -l pl.UTF-8
Dokumentacja do git-core.

%description doc -l fr.UTF-8
Javadoc pour git-core.

%package daemon-inetd
Summary:	Files necessary to run git-daemon as an inetd service
Summary(pl.UTF-8):	Pliki niezbędne do uruchomienia git-daemona w trybie usługi inetd
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	setup >= 2.4.11-1
Provides:	git-core-daemon
Obsoletes:	git-core-daemon
Obsoletes:	git-core-daemon-standalone

%description daemon-inetd
Git-daemon is a really simple TCP git daemon that can serve git
repositories. This package provides all necessarry files to run
git-daemon as an inetd service.

%description daemon-inetd -l pl.UTF-8
Git-daemon to prosty demon git korzystający z protokołu TCP do
udostępniania repozytoriów git. Ten pakiet dostarcza pliki potrzebne
do uruchomienia git-demona w trybie usługi inetd.

%package daemon-standalone
Summary:	Files necessary to run git-daemon as a standalone service
Summary(pl.UTF-8):	Pliki niezbędne do uruchomienia git-daemona w trybie usługi samodzielnej
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Provides:	git-core-daemon
Obsoletes:	git-core-daemon
Obsoletes:	git-core-daemon-inetd

%description daemon-standalone
Git-daemon is a really simple TCP git daemon that can serve git
repositories. This package provides all necessarry files to run
git-daemon as an standalone service.

%description daemon-standalone -l pl.UTF-8
Git-daemon to prosty demon git korzystający z protokołu TCP do
udostępniania repozytoriów git. Ten pakiet dostarcza pliki potrzebne
do uruchomienia git-daemona w trybie usługi samodzielnej.

%package devel
Summary:	Header files for git-core
Summary(pl.UTF-8):	Pliki nagłówkowe dla git-core
Group:		Development/Libraries
Requires:	zlib-devel

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
gitk displays changes in a repository or a selected set of commits.
This includes visualizing the commit graph, showing information
related to each commit, and the files in the trees of each revision.

Historically, gitk was the first repository browser. It's written in
Tcl/Tk and started off in a separate repository but was later merged
into the main git repository.

%description gitk -l pl.UTF-8
gitk wyświetla zmiany w repozytorium lub wybranym zbiorze commitów.
Oznacza to wizualizację grafu commitów, wyświetlanie informacji
związanych z każdym z commitów oraz listę plików dla każdej rewizji.

Z historycznego punktu widzenia gitk był pierwszą przeglądarką
repozytorium git. Napisany jest w Tcl/Tk i początkowo był rozwijany w
osobnym repozytorium, ale z czasem został włączony do głównego
repozytorium gita.

%package gitweb
Summary:	Web frontend to git
Summary(pl.UTF-8):	Frontend WWW do gita
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	webapps
Requires:	webserver(alias)
Requires:	webserver(cgi)
Suggests:	webserver(setenv)

%description gitweb
This package provides a web interface for browsing git repositories.

%description gitweb -l pl.UTF-8
Pakiet ten dostarcza interfejs WWW do przeglądania repozytoriów gita.

%package gitview
Summary:	A GTK+ based repository browser for git
Summary(pl.UTF-8):	Oparta na GTK+ przeglądarka repozytorium gita
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	python >= 1:2.4
Requires:	python-pycairo >= 1.0
Requires:	python-pygobject
Requires:	python-pygtk-gtk >= 2:2.8
Suggests:	python-gnome-desktop-gtksourceview

%description gitview
A GTK+ based repository browser for git.

%description gitview -l pl.UTF-8
Oparta na GTK+ przeglądarka repozytorium gita.

%package gui
Summary:	Tcl/Tk interface to the Git version control system
Summary(pl.UTF-8):	Napisany w Tcl/Tk interfejs do systemu kontroli wersji Git
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	tk
Requires:	xdg-utils
Suggests:	meld

%description gui
Displays changes in a repository or a selected set of commits. This
includes visualizing the commit graph, showing information related to
each commit, and the files in the trees of each revision.

Historically, gitk was the first repository browser. It's written in
Tcl/Tk and started off in a separate repository but was later merged
into the main git repository.

%description gui -l pl.UTF-8
Wyświetla zmiany w repozytorium lub wybranym zbiorze commitów. Oznacza
to wizualizację grafu commitów, wyświetlanie informacji związanych z
każdym z commitów oraz listę plików dla każdej rewizji.

Z punktu widzenia historii, gitk był pierwszą przeglądarką
repozytorium git. Napisany jest w Tcl/Tk i początkowo był rozwijany w
osobnym repozytorium, ale z czasem został włączony do głównego
repozytorium gita.

%package svn
Summary:	Subversion support for Git
Summary(pl.UTF-8):	Obsługa Subversion dla Gita
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Encode
Requires:	perl-Term-ReadKey

%description svn
Subversion support for Git.

%description svn -l pl.UTF-8
Obsługa Subversion dla Gita.

%package cvs
Summary:	CVS support for Git
Summary(pl.UTF-8):	Obsługa CVS dla Gita
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	cvsps >= 2.1-2
Requires:	rcs

%description cvs
CVS support for Git.

%description cvs -l pl.UTF-8
Obsługa CVS dla Gita.

%package arch
Summary:	Git tools for importing Arch repositories
Summary(pl.UTF-8):	Narzędzia Gita do importowania repozytoriów Archa
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	tla

%description arch
Git tools for importing Arch repositories.

%description arch -l pl.UTF-8
Narzędzia Gita do importowania repozytoriów Archa.

%package email
Summary:	Git tools for sending email
Summary(pl.UTF-8):	Narzędzia Gita do wysyłania poczty
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description email
Git tools for sending email.

%description email -l pl.UTF-8
Narzędzia Gita do wysyłania poczty.

%package -n bash-completion-git
Summary:	bash-completion for git
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla gita
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-git
This package provides bash-completion for git.

%description -n bash-completion-git -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla gita.

%package -n perl-Git
Summary:	Perl interface to the Git version control system
Summary(pl.UTF-8):	Perlowy interfejs do systemu kontroli wersji Git
Group:		Development/Languages/Perl
Obsoletes:	perl-git-core

%description -n perl-Git
This module provides Perl scripts easy way to interface the Git
version control system. The modules have an easy and well-tested way
to call arbitrary Git commands; in the future, the interface will also
provide specialized methods for doing easily operations which are not
totally trivial to do over the generic command interface.

%description -n perl-Git -l pl.UTF-8
Ten moduł umożliwia skryptom Perla współpracę z systemem kontroli
wersji Git. W łatwy i dobrze przetestowany sposób pozwala wywoływać
dowolne polecenia Gita; w przyszłości interfejs udostępni także
specjalne metody do łatwego wykonywania operacji nietrywialnych do
wykonania przy użyciu ogólnego interfejsu poleceń.

%package -n python-Git
Summary:	Python Git remote helpers for non-git repositories
Summary(pl.UTF-8):	Pythonowe zdalne moduły pomocnicze dla repozytoriów niegitowych
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-Git
This package contains Python git_repote_helpers package - Git remote
helpers for non-git repositories.

%description -n python-Git -l pl.UTF-8
Ten pakiet zawiera pakiet Pythona git_remote_helpers - zdalne moduły
pomocnicze Gita dla repozytoriów niegitowych.

%package -n vim-syntax-gitcommit
Summary:	Vim syntax: gitcommit
Summary(pl.UTF-8):	Składnia dla Vima: gitcommit
Group:		Applications/Editors/Vim
Requires:	%{name} = %{version}-%{release}
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3

%description -n vim-syntax-gitcommit
This plugin provides syntax highlighting for git's commit messages.

%description -n vim-syntax-gitcommit -l pl.UTF-8
Ta wtyczka dostarcza podświetlanie składni dla treści commitów gita.

%prep
%setup -q -n git-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--sysconfdir=%{_sysconfdir}/git-core \
	--with-openssl

echo "BLK_SHA1=1" >> config.mak

%{__make} \
	INSTALLDIRS=vendor \
	GITWEB_CONFIG="%{webappdir}/gitweb.conf" \
	GITWEB_PROJECTROOT="/var/lib/git" \
	GITWEB_CSS="/gitweb/gitweb.css" \
	GITWEB_LOGO="/gitweb/git-logo.png" \
	GITWEB_FAVICON="/gitweb/git-favicon.png" \
	V=1

# use DOCBOOK_XSL_172=1 to fix 'the ".ft C" problem' in generated manpages.
%{?with_doc:%{__make} -C Documentation V=1 DOCBOOK_XSL_172=1}

%if %{with tests}
%if %{without tests_cvs}
rm t/t*cvs*.sh || :
%endif
%{!?with_svn:GIT_SKIP_TESTS='t91??'} %{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name}/xdiff,%{_localstatedir}/lib/git}
install -d $RPM_BUILD_ROOT{%{appdir},%{cgibindir},%{webappdir}}
install -d $RPM_BUILD_ROOT/etc/{sysconfig/rc-inetd,rc.d/init.d}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/git-core/gitconfig
[init]
	templatedir = %{_sysconfdir}/%{name}/templates
EOF

%{__make} install \
	INSTALLDIRS=vendor \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} -C Documentation install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

# copy templates except sample hooks
cp -a $RPM_BUILD_ROOT%{_datadir}/%{name}/templates $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/templates/hooks/*.sample

# header files and lib
cp -p *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -a compat $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -p xdiff/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/xdiff
cp -p libgit.a $RPM_BUILD_ROOT%{_libdir}
cp -p xdiff/lib.a $RPM_BUILD_ROOT%{_libdir}/libgit_xdiff.a

# bash completion
install -d $RPM_BUILD_ROOT/etc/bash_completion.d
cp -p contrib/completion/git-completion.bash $RPM_BUILD_ROOT/etc/bash_completion.d

# vim syntax
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
cat > $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax/gitcommit.vim << 'EOF'
autocmd BufNewFile,BufRead *.git/COMMIT_EDITMSG    setf gitcommit
autocmd BufNewFile,BufRead *.git/config,.gitconfig setf gitconfig
autocmd BufNewFile,BufRead git-rebase-todo         setf gitrebase
autocmd BufNewFile,BufRead .msg.[0-9]*
	\ if getline(1) =~ '^From.*# This line is ignored.$' |
	\   setf gitsendemail |
	\ endif
autocmd BufNewFile,BufRead *.git/**
	\ if getline(1) =~ '^\x\{40\}\>\|^ref: ' |
	\   setf git |
	\ endif
EOF

# gitweb
mv $RPM_BUILD_ROOT{%{appdir},%{cgibindir}}/gitweb.cgi
ln -s %{cgibindir}/gitweb.cgi $RPM_BUILD_ROOT%{appdir}/gitweb.cgi
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{webappdir}/gitweb.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{webappdir}/apache.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{webappdir}/httpd.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{webappdir}/lighttpd.conf

# gitview
install -p contrib/gitview/gitview $RPM_BUILD_ROOT%{_bindir}

# git-daemon related files
cp -a %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/git-daemon
cp -a %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/git-daemon
install -p %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/git-daemon

# paths cleanup
sed -e 's,@libdir@,%{_libdir},g' -i $RPM_BUILD_ROOT/etc/rc.d/init.d/git-daemon
sed -e 's,@libdir@,%{_libdir},g' -i $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/git-daemon

# hardlink
ln -f $RPM_BUILD_ROOT%{_bindir}/{git,git-receive-pack}
ln -f $RPM_BUILD_ROOT%{_bindir}/{git,git-upload-archive}
ln -f $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_bindir}}/git-shell
ln -f $RPM_BUILD_ROOT{%{_libdir}/%{name},%{_bindir}}/git-upload-pack

# remove unneeded files
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Git/.packlist
%py_postclean

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
%find_lang git

%clean
rm -rf $RPM_BUILD_ROOT

%post daemon-inetd
%service -q rc-inetd reload

%postun daemon-inetd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%post daemon-standalone
/sbin/chkconfig --add git-daemon
%service git-daemon restart "git-daemon"

%preun daemon-standalone
if [ "$1" = "0" ]; then
	%service git-daemon stop
	/sbin/chkconfig --del git-daemon
fi

%triggerin gitweb -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{webapp}

%triggerun gitweb -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{webapp}

%triggerin gitweb -- apache < 2.2.0, apache-base
%webapp_register httpd %{webapp}

%triggerun gitweb -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{webapp}

%triggerin gitweb -- lighttpd
%webapp_register lighttpd %{webapp}

%triggerun gitweb -- lighttpd
%webapp_unregister lighttpd %{webapp}

%files -f git.lang
%defattr(644,root,root,755)
%doc README contrib
%attr(755,root,root) %{_bindir}/git
%attr(755,root,root) %{_bindir}/git-receive-pack
%attr(755,root,root) %{_bindir}/git-shell
%attr(755,root,root) %{_bindir}/git-upload-archive
%attr(755,root,root) %{_bindir}/git-upload-pack
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}

%if %{with doc}
%{_mandir}/man1/git-*.1*
%exclude %{_mandir}/man1/git-svn.1*
%exclude %{_mandir}/man1/git-cvs*.1*
%exclude %{_mandir}/man1/git-remote-helpers.1*
%{_mandir}/man1/git.1*
%{_mandir}/man5/gitattributes.5*
%{_mandir}/man5/githooks.5*
%{_mandir}/man5/gitignore.5*
%{_mandir}/man5/gitmodules.5*
%{_mandir}/man5/gitrepository-layout.5*
%{_mandir}/man7/gitcli.7*
%{_mandir}/man7/gitcore-tutorial.7*
%{_mandir}/man7/gitcredentials.7*
%{_mandir}/man7/gitdiffcore.7*
%{_mandir}/man7/gitglossary.7*
%{_mandir}/man7/gitnamespaces.7*
%{_mandir}/man7/gitrevisions.7*
%{_mandir}/man7/gittutorial-2.7*
%{_mandir}/man7/gittutorial.7*
%{_mandir}/man7/gitworkflows.7*
%endif

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*-*
%attr(755,root,root) %{_libdir}/%{name}/git
%{_libdir}/%{name}/mergetools

%exclude %{_libdir}/%{name}/git-gui
%exclude %{_libdir}/%{name}/git-svn
%exclude %{_libdir}/%{name}/git-archimport
%exclude %{_libdir}/%{name}/git-cvs*
%exclude %{_libdir}/%{name}/git-instaweb
%exclude %{_libdir}/%{name}/git-remote-testgit
%exclude %{_libdir}/%{name}/*email*

%{_datadir}/%{name}

%{_localstatedir}/lib/git

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc Documentation/RelNotes*
%doc Documentation/*.html Documentation/howto Documentation/technical
%endif

%files daemon-inetd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/git-daemon

%files daemon-standalone
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/git-daemon
%attr(754,root, root) /etc/rc.d/init.d/git-daemon

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/libgit.a
%{_libdir}/libgit_xdiff.a

%files gitk
%defattr(644,root,root,755)
%if %{with doc}
%{_mandir}/man1/gitk.1*
%endif
%attr(755,root,root) %{_bindir}/gitk
%dir %{_datadir}/gitk
%dir %{_datadir}/gitk/lib
%dir %{_datadir}/gitk/lib/msgs
%lang(de) %{_datadir}/gitk/lib/msgs/de.msg
%lang(es) %{_datadir}/gitk/lib/msgs/es.msg
%lang(fr) %{_datadir}/gitk/lib/msgs/fr.msg
%lang(hu) %{_datadir}/gitk/lib/msgs/hu.msg
%lang(it) %{_datadir}/gitk/lib/msgs/it.msg
%lang(ja) %{_datadir}/gitk/lib/msgs/ja.msg
%lang(pt_BR) %{_datadir}/gitk/lib/msgs/pt_br.msg
%lang(ru) %{_datadir}/gitk/lib/msgs/ru.msg
%lang(sv) %{_datadir}/gitk/lib/msgs/sv.msg

%files gitweb
%defattr(644,root,root,755)
%doc gitweb/{README,INSTALL}
%dir %{webappdir}
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,http) %{webappdir}/gitweb.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/apache.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/httpd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/lighttpd.conf
%attr(755,root,root) %{cgibindir}/gitweb.cgi
%{appdir}
%attr(755,root,root) %{_libdir}/%{name}/git-instaweb
%if %{with doc}
%{_mandir}/man1/gitweb.1*
%{_mandir}/man5/gitweb.conf.5*
%endif

%files gitview
%defattr(644,root,root,755)
%doc contrib/gitview/gitview.txt
%attr(755,root,root) %{_bindir}/gitview

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/git-gui
%dir %{_datadir}/git-gui
%dir %{_datadir}/git-gui/lib
%dir %{_datadir}/git-gui/lib/msgs
%{_datadir}/git-gui/lib/git-gui.ico
%{_datadir}/git-gui/lib/tclIndex
%{_datadir}/git-gui/lib/*.js
%{_datadir}/git-gui/lib/*.tcl
%lang(de) %{_datadir}/git-gui/lib/msgs/de.msg
%lang(el) %{_datadir}/git-gui/lib/msgs/el.msg
%lang(fr) %{_datadir}/git-gui/lib/msgs/fr.msg
%lang(hu) %{_datadir}/git-gui/lib/msgs/hu.msg
%lang(it) %{_datadir}/git-gui/lib/msgs/it.msg
%lang(ja) %{_datadir}/git-gui/lib/msgs/ja.msg
%lang(nb) %{_datadir}/git-gui/lib/msgs/nb.msg
%lang(pt_br) %{_datadir}/git-gui/lib/msgs/pt_br.msg
%lang(ru) %{_datadir}/git-gui/lib/msgs/ru.msg
%lang(sv) %{_datadir}/git-gui/lib/msgs/sv.msg
%lang(zh_CN) %{_datadir}/git-gui/lib/msgs/zh_cn.msg

%files svn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/git-svn
%if %{with doc}
%{_mandir}/man1/git-svn.1*
%endif

%files cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/git-cvsserver
%attr(755,root,root) %{_libdir}/%{name}/git-cvs*
%if %{with doc}
%{_mandir}/man1/git-cvs*.1*
%{_mandir}/man7/gitcvs-migration.7*
%endif

%files arch
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/git-archimport
%if %{with doc}
%{_mandir}/man1/git-archimport.1*
%endif

%files email
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/*email*
%if %{with doc}
%{_mandir}/man1/*email*.1*
%endif

%files -n bash-completion-git
%defattr(644,root,root,755)
/etc/bash_completion.d/git-completion.bash

%files -n perl-Git
%defattr(644,root,root,755)
%{perl_vendorlib}/Git.pm
%{perl_vendorlib}/Git
%{_mandir}/man3/Git*.3pm*

%files -n python-Git
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/git-remote-testgit
%dir %{py_sitescriptdir}/git_remote_helpers
%{py_sitescriptdir}/git_remote_helpers/*.py[co]
%dir %{py_sitescriptdir}/git_remote_helpers/git
%{py_sitescriptdir}/git_remote_helpers/git/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/git_remote_helpers*.egg-info
%endif
%if %{with doc}
%{_mandir}/man1/git-remote-helpers.1*
%endif

%files -n vim-syntax-gitcommit
%defattr(644,root,root,755)
%doc contrib/vim/README
%{_datadir}/vim/vimfiles/syntax/gitcommit.vim
