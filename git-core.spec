# TODO: documentation
Summary:	The stupid content tracker
Name:		git-core
Version:	0.99.8
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.kernel.org/pub/software/scm/git/%{name}-%{version}.tar.bz2
# Source0-md5:	0fb209de06352923b66ef1ca50e1b3b7
BuildRequires:	curl-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"git" can mean anything, depending on your mood.

 - random three-letter combination that is pronounceable, and not
   actually used by any common UNIX command.  The fact that it is a
   mispronunciation of "get" may or may not be relevant.
 - stupid. contemptible and despicable. simple. Take your pick from the
   dictionary of slang.
 - "global information tracker": you're in a good mood, and it actually
   works for you. Angels sing, and a light suddenly fills the room.
 - "goddamn idiotic truckload of sh*t": when it breaks

This is a stupid (but extremely fast) directory content manager.  It
doesn't do a whole lot, but what it 'does' do is track directory
contents efficiently.

%prep
%setup -q
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=/usr \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
