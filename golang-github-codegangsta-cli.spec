# http://github.com/codegangsta/cli
%global goipath         github.com/codegangsta/cli
Version:                1.20.0

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package for building command line apps in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

Patch0:         0001-fix-ineffective-assigns.patch

BuildRequires: golang(gopkg.in/urfave/cli.v1)
BuildRequires: golang(github.com/BurntSushi/toml)
BuildRequires: golang(gopkg.in/yaml.v2)

%description
cli.go is simple, fast, and fun package for building command line apps in Go.
The goal is to enable developers to write fast and distributable command line
applications in an expressive way.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup -p1
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.20.0-1
- Release 1.20.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.17.0-10
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.17.0-8.git01857ac
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.17.0-7
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.0-2
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu May 26 2016 jchaloup <jchaloup@redhat.com> - 1.17.0-1
- Bump to upstream 01857ac33766ce0c93856370626f9799281c14f4
  related: #1248680

* Wed Mar 16 2016 jchaloup <jchaloup@redhat.com> - 1.2.0-9
- Bump to upstream c31a7975863e7810c92e2e288a9ab074f9a88f29
  related: #1248680

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 jchaloup <jchaloup@redhat.com> - 1.2.0-6
- Bump to upstream 942282e931e8286aa802a30b01fa7e16befb50f3
  related: #1248680

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 1.2.0-5
- Update to spec-2.1
  related: #1248680

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 1.2.0-4
- Update spec file to spec-2.0
  resolves: #1248680

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 jchaloup <jchaloup@redhat.com> - 1.2.0-2
- Bump to upstream b490b5e35d7e246da681819c9e6bf80758222b97
  related: #1114175

* Thu Aug 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2.0-1
- bump to v1.2.0

* Wed Jul 30 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-1
- 27ecc97192df1bf053a22b04463f2b51b8b8373e tagged 1.1.0
- manage el6 archfulness separately
- remove attr and defattr for fedora

* Fri Jul 25 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-4
- update to master commit 27ecc97192df1bf053a22b04463f2b51b8b8373e

* Mon Jul 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-3
- correct cp args

* Wed Jul 16 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2
- From: Vincent Batts <vbatts@fedoraproject.org>
- remove boiler-plate, to use golang rpm macros instead
- preserve timestamps of copied source
- don't own directories that golang owns

* Sat Jun 28 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1
- Initial fedora package

