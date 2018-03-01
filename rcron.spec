Summary: tool to setup cron jobs redundancy and failover over groups of machines
Name: rcron
Version: 0.1.0
Release: 1
License: GPL
Group: Applications/System
URL: https://github.com/jasonwee/rcron

Source0: rcron-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: byacc flex gcc

%description
rcron is a minimal tool aiming to help sysadmins in setting up cron jobs 
redundancy and failover over groups of machines. It only ensures that a job 
installed on several machines will only run on the active one at any time.

%prep
%setup

%build
%configure 
%{__make} 


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}



%files
%defattr(-, root, root, -)
%{_bindir}/rcron
%{_mandir}/man8/rcron.8.gz


%changelog
* Thu Mar  1 2018 Jason Wee <peichieh@gmail.com> 0.1.0-1
- Initial package.
