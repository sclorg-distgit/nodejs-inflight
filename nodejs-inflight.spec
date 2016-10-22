%{?scl:%scl_package nodejs-inflight}
%{!?scl:%global pkg_name %{name}}
%nodejs_find_provides_and_requires

Name:           %{?scl_prefix}nodejs-inflight
Version:        1.0.4
Release:        4%{?dist}
Summary:        Node.js inflight
License:        ISC
Group:          Development/Languages/Other
Url:            https://github.com/isaacs/inflight
Source:         http://registry.npmjs.org/inflight/-/inflight-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
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
%defattr(-,root,root,-)
%doc README.md LICENSE
%{nodejs_sitelib}/inflight

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-3
- Rebuilt with updated metapackage

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build

