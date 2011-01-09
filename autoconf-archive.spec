Name:           autoconf-archive
Version:        2011.01.02
Release:        %mkrel 1
Epoch:          0
Summary:        Autoconf Macro Archive
License:        GPL
Group:          Development/Other
URL:            http://autoconf-archive.cryp.to/
Source0:        http://ftpmirror.gnu.org/autoconf-archive/autoconf-archive-%{version}.tar.xz
Requires:       automake
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Autoconf Macro Archive aims to provide a collection of reusable Autoconf
macros as free software. The archive currently features more than 500 macros
which perform portability tests ranging from compiler support for weird
language extensions to automatic generation of sophisticated Automake rules.
All these macros have been contributed by friendly supporters of the cause
from all over the Internet; this archive is merely a distribution of other
people's efforts.

%prep
%setup -q -n autoconf-archive-%{version}

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} %{buildroot}%{_datadir}/autoconf-archive/{AUTHORS,COPYING,README}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING INSTALL README
%{_datadir}/autoconf-archive
%{_datadir}/aclocal/*
%{_infodir}/*
