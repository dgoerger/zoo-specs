%global packname swirl
%global packrel 1
%global debug_package %{nil}

%define coursesdir Courses

Name:             R-%{packname}
Version:          2.4.3
Release:          1%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
# let's also bundle R-swirl_courses: https://github.com/swirldev/swirl_courses
Source1:          swirl_courses.30b1b1e.tar.xz
Patch0:           534_swirl_userdata.patch
License:          GPLv2+
URL:              http://cran.r-project.org/src/contrib
Group:            Applications/Engineering
Summary:          Interactive learning environment for R
BuildRequires:    R-devel
BuildRequires:    R-RCurl, R-digest, R-testthat, R-stringr, R-httr, R-yaml
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-RCurl, R-digest, R-testthat, R-stringr, R-httr, R-yaml

%description
R interface to swirl. swirl is a software package for the R programming
language that turns the R console into an interactive learning
environment. Users receive immediate feedback as they are guided through
self-paced lessons in data science and R programming.

%prep
%setup -q -c -n %{packname}
cp -p %SOURCE1 .
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

# don't conflict with R-swirl_courses package
#rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/Courses

# copy in courses
tar -xf  %{_builddir}/%{packname}/swirl_courses.30b1b1e.tar.xz -C %{buildroot}%{_libdir}/R/library/%{packname}/%{coursesdir}

%check
# needed to pass the test-encoding.R#27
export LC_ALL="en_US.UTF-8"
%{_bindir}/R CMD check %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/test/
%{_libdir}/R/library/%{packname}/Courses/

%changelog
* Sat Jun 10 2017 David Goerger <david.goerger@yale.edu> - 2.4.3-1
- update to 2.4.3

* Wed Sep 07 2016 David Goerger <its-sa@yale.edu> 2.4.2-2
- update to 2.4.2
- note that the test suite only passes with LC_ALL="en_US.UTF-8"

* Tue Jul 26 2016 David Goerger <its-sa@yale.edu> 2.2.21-1
- initial package creation
