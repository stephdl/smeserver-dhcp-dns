%define name smeserver-dhcp-dns
%define version 1.1.1
%define release 5

Summary: contrib to update dynamically the dns data
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
URL: http://www.contribs.org
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 9.0
Requires: perl-Text-DHCPparse
AutoReqProv: no

%description
Implementation of some features arround dhcp to dynamically update dns data file whenever the dhcp file changes.
This eliminates the 'pc-0001' etc. default names.

%changelog
* Tue May 13 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.0-1
- First release for SME Server 9.0
- Thanks to John Crisp, Stefano Zamboni and Rick Jones
- This contribs is made from the solution of Stefano Zamboni [SME:2388] 
- and the original idea of Rick Jones.

* Sun Mar 20 2005 Rick Jones <rick@activeservice.co.uk>
- [1.0-1]
- First complete release, includes resolution of client name clashes
- (thanks to Placido Sanchez for suggestions and load-testing)
- also ignores expired entries in the leases file

* Fri Apr 30 2004 Rick Jones <rick@activeservice.co.uk>
- [0.9-rc1]
- First provisional release, added GPL & README

* Fri Apr 30 2004 Rick Jones <rick@activeservice.co.uk>
- [0.2-2]
- Patch hostentries web-panel to allow non-IP entry of remote host,
- allows Cname support to be used (un-patch when RPM removed)

* Fri Apr 23 2004 Rick Jones <rick@activeservice.co.uk>
- [0.2-1]
- Handle static IPs, replaces 50domainARecords with 60hostARecords

* Thu Apr 22 2004 Rick Jones <rick@activeservice.co.uk>
- [0.1-3]
- Regenerate old DNS data after RPM removal
- Minor tidying

* Thu Apr 22 2004 Rick Jones <rick@activeservice.co.uk>
- [0.1-2]
- Moved actual daemon code into dhcp-dnsd, run just execs (better for ps)
- Add missing "run" file for log directory, and create /var/log directory
- Add some logging output
- Remove rc files (service is up by default, no startup needed)
- Re-arrange initialisation & cleanup

* Sun Apr 18 2004 Rick Jones <rick@activeservice.co.uk>
- [0.1-1]
- Initial beta release



%prep
%setup
%build
perl createlinks


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
#%attr(744,root,root) /var/service/dhcp-dns/dhcp-dns
%attr(755,root,root) /var/service/dhcp-dns/run

