Name:		autoconf-archive
Version:	2015.09.25
Release:	1
Summary:	The Autoconf Macro Archive
Group:		Development/Other
License:	GPLv3+ with exceptions
URL:		http://www.gnu.org/software/autoconf-archive/
Source0:	ftp://ftp.gnu.org:21/gnu/autoconf-archive/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texinfo
Requires:	autoconf

%description
The GNU Autoconf Archive is a collection of more than 450 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

# remove dir file which will be generated by /sbin/install-info
rm -f %{buildroot}%{_infodir}/dir

# document files are installed another location
rm -rf %{buildroot}%{_datadir}/%{name}

%files
%doc AUTHORS COPYING* ChangeLog NEWS README TODO
%{_datadir}/aclocal/*.m4
%{_infodir}/autoconf-archive.info*
