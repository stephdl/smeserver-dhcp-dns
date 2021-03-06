%define name smeserver-dhcp-dns
%define version 1.2.0
%define release 2

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
Requires: e-smith-release >= 8.0
AutoReqProv: no

%description
Implementation of some features arround dhcp to dynamically update dns data file whenever the dhcp file changes.
This eliminates the 'pc-0001' etc. default names.

%changelog
* Thu Jul 30 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-2
- finished lease are now prohibited

* Sat Jul 25 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-1
- enhancement following the bug [SME: 2388]
- e-smith-tinydns-2.4.0_add_hostname_following_dhcpdleases_hostname.patch
- waiting a release to the core, it is now a contrib for sme8

* Wed Jun 18 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.2-1
- correction of file 65dhcpARecords

* Sun May 18 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.0-12
- add a tinydns expand-template on event dhcp-dns
- add a restart dhcp-dns to signal-event dhcp-dns
- minor correction on event->action name

* Tue May 13 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.0-8
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
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /var/service/dhcp-dns/dhcp-dns 'attr(0750,root,root)' \
    --file /var/service/dhcp-dns/run 'attr(0750,root,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist
%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun

%post

%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
