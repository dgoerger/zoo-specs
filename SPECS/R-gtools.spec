%global packname  gtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.5.0
Release:          1%{?dist}
Summary:          Various R Programming Tools

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   
# Suggests:  
# LinkingTo:
# Enhances:





BuildRequires:    R-devel tex(latex) 



%description
Functions to assist in R programming, including: - assist in developing,
updating, and maintaining R and R packages ('ask', 'checkRVersion',
'getDependencies', 'keywords', 'scat'), - calculate the logit and inverse
logit transformations ('logit', 'inv.logit'), - test if a value is
missing, empty or contains only NA and NULL values ('invalid'), -
manipulate R's .Last function ('addLast'), - define macros ('defmacro'), -
detect odd and even integers ('odd', 'even'), - convert strings containing
non-ASCII characters (like single quotes) to plain ASCII ('ASCIIfy'), -
perform a binary search ('binsearch'), - sort strings containing both
numeric and character components ('mixedsort'), - create a factor variable
from the quantiles of a continuous variable ('quantcut'), - enumerate
permutations and combinations ('combinations', 'permutation'), - calculate
and convert between fold-change and log-ratio ('foldchange',
'logratio2foldchange', 'foldchange2logratio'), - calculate probabilities
and generate random numbers from Dirichlet distributions ('rdirichlet',
'ddirichlet'), - apply a function over adjacent subsets of a vector
('running'), - modify the TCP\_NODELAY ('de-Nagle') flag for socket
objects, - efficient 'rbind' of data frames, even if the column names
don't match ('smartbind'), - generate significance stars from p-values
('stars.pval'), - convert characters to/from ASCII codes.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Jun 30 2017 deg38 <> 3.5.0-1
- initial package for Fedora