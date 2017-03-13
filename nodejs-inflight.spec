%{?scl:%scl_package nodejs-inflight}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-inflight
Version:        1.0.5
Release:        1%{?dist}
Summary:        Node.js inflight
License:        ISC
Url:            https://github.com/isaacs/inflight
Source:         http://registry.npmjs.org/inflight/-/inflight-%{version}.tgz
BuildRequires:  %{?scl_prefix}runtime
BuildRequires:  %{?scl_prefix}nodejs-devel
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch


%description
Add callbacks to requests in flight to avoid async duplication 

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/inflight
cp -pr package.json inflight.js \
        %{buildroot}%{nodejs_sitelib}/inflight/

%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/inflight

%changelog
* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.5-1
- Updated with script

* Mon Sep 19 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-5
- Bump

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-3
- Rebuilt with updated metapackage

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build

