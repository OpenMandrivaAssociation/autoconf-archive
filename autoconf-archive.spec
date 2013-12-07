Name:		autoconf-archive
Version:	2013.06.09
Release:	2
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
%configure2_5x
%make

%install
%makeinstall_std

# remove dir file which will be generated by /sbin/install-info
rm -f %{buildroot}%{_infodir}/dir

# document files are installed another location
rm -rf %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* ChangeLog NEWS README TODO
%{_datadir}/aclocal/*.m4
%{_infodir}/autoconf-archive.info*


%changelog

* Tue May 29 2012 wally <wally> 2012.04.07-1.mga3
+ Revision: 249276
- new version 2012.04.07

* Mon Dec 26 2011 wally <wally> 2011.12.21-1.mga2
+ Revision: 187856
- new version 2011.12.21

* Tue Oct 18 2011 wally <wally> 2011.09.17-1.mga2
+ Revision: 156280
- imported package autoconf-archive


