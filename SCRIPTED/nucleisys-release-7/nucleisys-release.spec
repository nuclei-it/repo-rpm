Name:           nuclei-rpm-public
Version:        7
Release:        1%{?dist}
Summary:        Nuclei System Technology Public RPM Repository repository configuration

Group:          System Environment/Base
License:        GPLv2

URL:            https://github.com/nuclei-it/repo-rpm
Source0:        GPL
Source1:        nucleisys.repo
Source2:        RPM-GPG-KEY-NUCLEI-MANUAL-0
Source3:        RPM-GPG-KEY-NUCLEI-MANUAL-1

BuildArch:      noarch
Requires:       redhat-release >= %{version}

%description
This package contains the Nuclei System Technology Public RPM Repository repository
GPG key as well as configuration for yum.

%prep
#%setup -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 -t $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg %{SOURCE2} %{SOURCE3}

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Wed Dec 29 2021 Huanjie Zhu <james@nucleisys.com> 7-1
- Initial release
