#
# Conditional build:
%bcond_without	tests		# don't perform make test
%bcond_with	tests_cvs	# perform tests which use CVS
%bcond_without	tests_svn	# perform tests which use subversion
%bcond_without	doc		# skip building/packaging docs/manuals (takes some time)
%bcond_without	pcre		# perl-compatible regexes support
%bcond_without	gnome_keyring	# build without gnome keyring support

# for AC: --without doc --without gnome_keyring --without tests

%include	/usr/lib/rpm/macros.perl
Summary:	Distributed version control system focused on speed, effectivity and usability
Summary(pl.UTF-8):	Rozproszony system śledzenia treści skupiony na szybkości, wydajności i użyteczności
Name:		git-core
Version:	2.9.0
Release:	2
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.kernel.org/pub/software/scm/git/git-%{version}.tar.xz
# Source0-md5:	118ef1e3108ef0b858cd13b74395a59c
Source1:	%{name}-gitweb.conf
Source2:	%{name}-gitweb-httpd.conf
Source3:	%{name}-gitweb-lighttpd.conf
Source4:	%{name}.sysconfig
Source5:	%{name}.inet
Source6:	%{name}.init
Source7:	gitolite.pl
Patch0:		%{name}-tests.patch
Patch1:		%{name}-key-bindings.patch
Patch2:		%{name}-sysconfdir.patch
Patch3:		cherry-picked-commitlog.patch
Patch4:		%{name}-svn-exit-errors.patch
URL:		http://git-scm.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
%if "%{pld_release}" == "ac"
BuildRequires:	gettext-devel
%else
BuildRequires:	gettext-tools
%endif
%if %{with gnome_keyring}
BuildRequires:	libgnome-keyring-devel
BuildRequires:	pkgconfig
%endif
BuildRequires:	openssl-devel
%{?with_pcre:BuildRequires:	pcre-devel}
BuildRequires:	perl-Error > 0.15
BuildRequires:	perl-base
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.673
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
%if %{with tests_svn}
BuildRequires:	perl-subversion
BuildRequires:	subversion
%endif
Conflicts:	pdksh < 5.2.14-46
%endif
# git-sh-setup: sane_grep
Requires:	grep
# git-pull: printf
Requires:	coreutils
Requires:	perl-Error
Requires:	perl-Git = %{version}-%{release}
Requires:	sed
Suggests:	git-core-bzr
Suggests:	git-core-cvs
Suggests:	git-core-hg
Suggests:	git-core-p4
Suggests:	git-core-svn
Suggests:	less
Suggests:	openssh-clients
Suggests:	rsync
Obsoletes:	python-Git
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# html docs have links to txt files
%define		_noautocompressdoc	*.txt

%define		webapp		gitweb
%define		webappdir	%{_sysconfdir}/webapps/%{webapp}
%define		appdir		%{_datadir}/%{webapp}
%define		cgibindir	%{_prefix}/lib/cgi-bin
%define		gitcoredir	%{_prefix}/lib/%{name}
%define		_libexecdir	%{_prefix}/lib

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Documentation for git-core.

%description doc -l pl.UTF-8
Dokumentacja do git-core.

%package daemon-inetd
Summary:	Files necessary to run git-daemon as an inetd service
Summary(pl.UTF-8):	Pliki niezbędne do uruchomienia git-daemona w trybie usługi inetd
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	setup >= 2.4.11-1
Provides:	git-core-daemon
Obsoletes:	git-core-daemon
Obsoletes:	git-core-daemon-standalone
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description daemon-standalone
Git-daemon is a really simple TCP git daemon that can serve git
repositories. This package provides all necessarry files to run
git-daemon as an standalone service.

%description daemon-standalone -l pl.UTF-8
Git-daemon to prosty demon git korzystający z protokołu TCP do
udostępniania repozytoriów git. Ten pakiet dostarcza pliki potrzebne
do uruchomienia git-daemona w trybie usługi samodzielnej.

%package devel
Summary:	Git library with header files
Summary(pl.UTF-8):	Biblioteka Gita oraz pliki nagłówkowe
Group:		Development/Libraries
Requires:	zlib-devel

%description devel
Git library with header files.

%description devel -l pl.UTF-8
Biblioteka Gita oraz pliki nagłówkowe.

%package gitk
Summary:	Tcl/Tk interface to the Git version control system
Summary(pl.UTF-8):	Napisany w Tcl/Tk interfejs do systemu kontroli wersji Git
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	tk
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
Requires:	webserver(access)
Requires:	webserver(alias)
Requires:	webserver(cgi)
Suggests:	webserver(setenv)
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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

%package arch
Summary:	Git tools for importing Arch repositories
Summary(pl.UTF-8):	Narzędzia Gita do importowania repozytoriów Archa
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	tla
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description arch
Git tools for importing Arch repositories.

%description arch -l pl.UTF-8
Narzędzia Gita do importowania repozytoriów Archa.

%package bzr
Summary:	Git tools for working with bzr repositories
Summary(pl.UTF-8):	Narzędzia Gita do pracy z repozytoriami bzr
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	bzr
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description bzr
Git tools for working with bzr repositories.

%description bzr -l pl.UTF-8
Narzędzia Gita do pracy z repozytoriami bzr.

%package cvs
Summary:	CVS support for Git
Summary(pl.UTF-8):	Obsługa CVS dla Gita
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	cvsps >= 2.1-2
Requires:	rcs
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description cvs
CVS support for Git.

%description cvs -l pl.UTF-8
Obsługa CVS dla Gita.

%package hg
Summary:	Git tools for working with mercurial repositories
Summary(pl.UTF-8):	Narzędzia Gita do pracy z repozytoriami mercuriala
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	mercurial >= 1.8
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description hg
Git tools for working with mercurial repositories.

%description hg -l pl.UTF-8
Narzędzia Gita do pracy z repozytoriami mercuriala.

%package p4
Summary:	Git tools for working with Perforce depots
Summary(pl.UTF-8):	Narzędzia Gita do pracy z magazynami Perforce'a
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description p4
Git tools for working with Perforce depots.

%description p4 -l pl.UTF-8
Narzędzia Gita do pracy z magazynami Perforce'a.

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
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-git
This package provides bash-completion for git.

%description -n bash-completion-git -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla gita.

%package -n perl-Git
Summary:	Perl interface to the Git version control system
Summary(pl.UTF-8):	Perlowy interfejs do systemu kontroli wersji Git
Group:		Development/Languages/Perl
Obsoletes:	perl-git-core
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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

%package -n gnome-keyring-git-core
Summary:	GNOME Keyring authentication provider for Git
Summary(pl.UTF-8):	Moduł uwierzytelniający GNOME Keyring dla Git
Group:		X11/Applications
URL:		http://git-scm.com/docs/gitcredentials.html
Requires:	%{name} = %{version}-%{release}

%description -n gnome-keyring-git-core
Authentication provider module for Git which allows git client to
authenticate using GNOME Keyring.

You need to register it with:
- git config --global credential.helper gnome-keyring

%description -n gnome-keyring-git-core -l pl.UTF-8
Moduł uwierzytelniający dla Subversion pozwalający klientom git
uwierzytelniać się przy użyciu mechanizmu GNOME Keyring.

Moduł trzeba zarejestrować poleceniem:
- git config --global credential.helper gnome-keyring

%prep
%setup -q -n git-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%{__rm} {Documentation/technical,contrib/emacs,contrib/credential/gnome-keyring}/.gitignore

# we build things in contrib but want to have it clean for doc purporses, too
cp -a contrib contrib-doc

%build
%{__aclocal}
%{__autoconf}
%configure \
	--sysconfdir=%{_sysconfdir}/git-core \
	%{?with_pcre:--with-libpcre} \
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

%{__make} -C contrib/subtree

%if %{with gnome_keyring}
%{__make} -C contrib/credential/gnome-keyring
%endif

%if %{with doc}
%{__make} -C Documentation \
	MAN_BASE_URL=file://%{_docdir}/%{name}-doc-%{version}/ \
	V=1
%endif

%if %{with tests}
%if %{without tests_cvs}
%{__rm} t/t*cvs*.sh || :
%endif
%{!?with_tests_svn:GIT_SKIP_TESTS='t91??'} %{__make} test
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
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}/block-sha1
cp -p block-sha1/sha1.h $RPM_BUILD_ROOT%{_includedir}/%{name}/block-sha1
cp -p libgit.a $RPM_BUILD_ROOT%{_libdir}
cp -p xdiff/lib.a $RPM_BUILD_ROOT%{_libdir}/libgit_xdiff.a
cp -p {Makefile,config.mak,config.mak.autogen,config.mak.uname} $RPM_BUILD_ROOT%{_includedir}/%{name}

%{__make} -C contrib/subtree install \
	libexecdir=%{gitcoredir} \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} -C contrib/subtree install-man \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gnome_keyring}
install -p contrib/credential/gnome-keyring/git-credential-gnome-keyring $RPM_BUILD_ROOT%{gitcoredir}
%endif

# bash completion
install -d $RPM_BUILD_ROOT%{bash_compdir}
cp -p contrib/completion/git-completion.bash $RPM_BUILD_ROOT%{bash_compdir}/git

# Install git-prompt.sh
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/completion
cp -p contrib/completion/git-prompt.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/completion

# Install bzr and hg remote helpers from contrib
install -p contrib/remote-helpers/git-remote-{bzr,hg} $RPM_BUILD_ROOT%{gitcoredir}

# gitweb
mv $RPM_BUILD_ROOT{%{appdir},%{cgibindir}}/gitweb.cgi
ln -s %{cgibindir}/gitweb.cgi $RPM_BUILD_ROOT%{appdir}/gitweb.cgi
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{webappdir}/gitweb.conf
cp -p %{SOURCE7} $RPM_BUILD_ROOT%{webappdir}/gitolite.pl
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{webappdir}/apache.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{webappdir}/httpd.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{webappdir}/lighttpd.conf

# gitview
install -p contrib/gitview/gitview $RPM_BUILD_ROOT%{_bindir}

# git-daemon related files
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/git-daemon
cp -p %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/git-daemon
install -p %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/git-daemon

# paths cleanup
sed -e 's,@libdir@/git-core,%{gitcoredir},g' -i $RPM_BUILD_ROOT/etc/rc.d/init.d/git-daemon
sed -e 's,@libdir@/git-core,%{gitcoredir},g' -i $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/git-daemon

# same file, link
ln -sf git $RPM_BUILD_ROOT%{_bindir}/git-receive-pack
ln -sf git $RPM_BUILD_ROOT%{_bindir}/git-upload-archive
ln -sf ../..%{gitcoredir}/git-shell $RPM_BUILD_ROOT%{_bindir}/git-shell
ln -sf ../..%{gitcoredir}/git-upload-pack $RPM_BUILD_ROOT%{_bindir}/git-upload-pack
ln -sf ../..%{gitcoredir}/git $RPM_BUILD_ROOT%{_bindir}/git

# convert all hardlinks to symlinks, as rpm fails to calculate it properly
# requiring excessive free space when it may not be available
# https://bugs.launchpad.net/pld-linux/+bug/1176337
find $RPM_BUILD_ROOT%{gitcoredir} -samefile $RPM_BUILD_ROOT%{gitcoredir}/git > files
for f in $(cat files); do
	f=${f#$RPM_BUILD_ROOT%{gitcoredir}/}
	test $f = git && continue
	ln -snf git $RPM_BUILD_ROOT%{gitcoredir}/$f
done

# few others
ln -snf git-gui $RPM_BUILD_ROOT%{gitcoredir}/git-citool
ln -snf git-remote-http $RPM_BUILD_ROOT%{gitcoredir}/git-remote-https
ln -snf git-remote-http $RPM_BUILD_ROOT%{gitcoredir}/git-remote-ftp
ln -snf git-remote-http $RPM_BUILD_ROOT%{gitcoredir}/git-remote-ftps

# remove unneeded files
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Git/.packlist
%py_postclean

mv $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}
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
%doc README.md contrib-doc
%attr(755,root,root) %{_bindir}/git
%attr(755,root,root) %{_bindir}/git-receive-pack
%attr(755,root,root) %{_bindir}/git-shell
%attr(755,root,root) %{_bindir}/git-upload-archive
%attr(755,root,root) %{_bindir}/git-upload-pack
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}

%if %{with doc}
%{_mandir}/man1/git-*.1*
%exclude %{_mandir}/man1/git-archimport.1*
%exclude %{_mandir}/man1/git-svn.1*
%exclude %{_mandir}/man1/git-cvs*.1*
%exclude %{_mandir}/man1/git-imap-send*.1*
%exclude %{_mandir}/man1/*email*.1*
%{_mandir}/man1/git.1*
%{_mandir}/man1/gitremote-helpers.1*
%{_mandir}/man5/gitattributes.5*
%{_mandir}/man5/githooks.5*
%{_mandir}/man5/gitignore.5*
%{_mandir}/man5/gitmodules.5*
%{_mandir}/man5/gitrepository-layout.5*
%{_mandir}/man7/gitcli.7*
%{_mandir}/man7/gitcore-tutorial.7*
%{_mandir}/man7/gitcredentials.7*
%{_mandir}/man7/gitdiffcore.7*
%{_mandir}/man7/giteveryday.7*
%{_mandir}/man7/gitglossary.7*
%{_mandir}/man7/gitnamespaces.7*
%{_mandir}/man7/gitrevisions.7*
%{_mandir}/man7/gittutorial-2.7*
%{_mandir}/man7/gittutorial.7*
%{_mandir}/man7/gitworkflows.7*
%endif

%dir %{gitcoredir}
%attr(755,root,root) %{gitcoredir}/*-*
%attr(755,root,root) %{gitcoredir}/git
%dir %{gitcoredir}/mergetools
%{gitcoredir}/mergetools/*

%{_datadir}/%{name}
%{_localstatedir}/lib/git

# subpackages
%exclude %{gitcoredir}/*email*
%exclude %{gitcoredir}/*p4*
%exclude %{gitcoredir}/git-archimport
%exclude %{gitcoredir}/git-cvs*
%exclude %{gitcoredir}/git-gui
%exclude %{gitcoredir}/git-imap-send
%exclude %{gitcoredir}/git-instaweb
%exclude %{gitcoredir}/git-remote-bzr
%exclude %{gitcoredir}/git-remote-hg
%exclude %{gitcoredir}/git-remote-testsvn
%exclude %{gitcoredir}/git-svn
%exclude %{gitcoredir}/mergetools/p4merge
%if %{with gnome_keyring}
%exclude %{gitcoredir}/git-credential-gnome-keyring
%endif

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
%lang(bg) %{_datadir}/gitk/lib/msgs/bg.msg
%lang(ca) %{_datadir}/gitk/lib/msgs/ca.msg
%lang(de) %{_datadir}/gitk/lib/msgs/de.msg
%lang(es) %{_datadir}/gitk/lib/msgs/es.msg
%lang(fr) %{_datadir}/gitk/lib/msgs/fr.msg
%lang(hu) %{_datadir}/gitk/lib/msgs/hu.msg
%lang(it) %{_datadir}/gitk/lib/msgs/it.msg
%lang(ja) %{_datadir}/gitk/lib/msgs/ja.msg
%lang(pt_BR) %{_datadir}/gitk/lib/msgs/pt_br.msg
%lang(ru) %{_datadir}/gitk/lib/msgs/ru.msg
%lang(sv) %{_datadir}/gitk/lib/msgs/sv.msg
%lang(vi) %{_datadir}/gitk/lib/msgs/vi.msg

%files gitweb
%defattr(644,root,root,755)
%doc gitweb/{README,INSTALL}
%dir %{webappdir}
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/apache.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/httpd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{webappdir}/lighttpd.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,http) %{webappdir}/gitweb.conf
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,http) %{webappdir}/gitolite.pl
%attr(755,root,root) %{cgibindir}/gitweb.cgi
%{appdir}
%attr(755,root,root) %{gitcoredir}/git-instaweb
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
%attr(755,root,root) %{gitcoredir}/git-gui
%dir %{_datadir}/git-gui
%dir %{_datadir}/git-gui/lib
%dir %{_datadir}/git-gui/lib/msgs
%{_datadir}/git-gui/lib/git-gui.ico
%{_datadir}/git-gui/lib/tclIndex
%{_datadir}/git-gui/lib/*.js
%{_datadir}/git-gui/lib/*.tcl
%lang(bg) %{_datadir}/git-gui/lib/msgs/bg.msg
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
%lang(vi) %{_datadir}/git-gui/lib/msgs/vi.msg
%lang(zh_CN) %{_datadir}/git-gui/lib/msgs/zh_cn.msg

%files arch
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-archimport
%if %{with doc}
%{_mandir}/man1/git-archimport.1*
%endif

%files bzr
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-remote-bzr

%files cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/git-cvsserver
%attr(755,root,root) %{gitcoredir}/git-cvs*
%if %{with doc}
%{_mandir}/man1/git-cvs*.1*
%{_mandir}/man7/gitcvs-migration.7*
%endif

%files hg
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-remote-hg

%files p4
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-p4
%attr(755,root,root) %{gitcoredir}/mergetools/p4merge

%files svn
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-svn
%attr(755,root,root) %{gitcoredir}/git-remote-testsvn
%{perl_vendorlib}/Git/SVN
%{perl_vendorlib}/Git/SVN.pm
%if %{with doc}
%{_mandir}/man1/git-svn.1*
%endif
%{_mandir}/man3/Git::SVN::Editor.3pm*
%{_mandir}/man3/Git::SVN::Fetcher.3pm*
%{_mandir}/man3/Git::SVN::Memoize::YAML.3pm*
%{_mandir}/man3/Git::SVN::Prompt.3pm*
%{_mandir}/man3/Git::SVN::Ra.3pm*
%{_mandir}/man3/Git::SVN::Utils.3pm*

%files email
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-imap-send
%attr(755,root,root) %{gitcoredir}/*email*
%if %{with doc}
%{_mandir}/man1/*email*.1*
%{_mandir}/man1/*imap-send*.1*
%endif

%files -n bash-completion-git
%defattr(644,root,root,755)
%{bash_compdir}/git

%files -n perl-Git
%defattr(644,root,root,755)
%{perl_vendorlib}/Git.pm
%dir %{perl_vendorlib}/Git
%{perl_vendorlib}/Git/I18N.pm
%{perl_vendorlib}/Git/IndexInfo.pm
%{_mandir}/man3/Git.3pm*
%{_mandir}/man3/Git::I18N.3pm*

%if %{with gnome_keyring}
%files -n gnome-keyring-git-core
%defattr(644,root,root,755)
%attr(755,root,root) %{gitcoredir}/git-credential-gnome-keyring
%endif
