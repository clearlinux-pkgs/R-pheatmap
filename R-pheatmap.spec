#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pheatmap
Version  : 1.0.12
Release  : 11
URL      : https://cran.r-project.org/src/contrib/pheatmap_1.0.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pheatmap_1.0.12.tar.gz
Summary  : Pretty Heatmaps
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : R-RColorBrewer
BuildRequires : R-Rcpp
BuildRequires : R-gtable
BuildRequires : R-munsell
BuildRequires : R-scales
BuildRequires : buildreq-R

%description
over dimensions and appearance.

%prep
%setup -q -c -n pheatmap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552877711

%install
export SOURCE_DATE_EPOCH=1552877711
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pheatmap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pheatmap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pheatmap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  pheatmap || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pheatmap/DESCRIPTION
/usr/lib64/R/library/pheatmap/INDEX
/usr/lib64/R/library/pheatmap/Meta/Rd.rds
/usr/lib64/R/library/pheatmap/Meta/features.rds
/usr/lib64/R/library/pheatmap/Meta/hsearch.rds
/usr/lib64/R/library/pheatmap/Meta/links.rds
/usr/lib64/R/library/pheatmap/Meta/nsInfo.rds
/usr/lib64/R/library/pheatmap/Meta/package.rds
/usr/lib64/R/library/pheatmap/NAMESPACE
/usr/lib64/R/library/pheatmap/NEWS
/usr/lib64/R/library/pheatmap/R/pheatmap
/usr/lib64/R/library/pheatmap/R/pheatmap.rdb
/usr/lib64/R/library/pheatmap/R/pheatmap.rdx
/usr/lib64/R/library/pheatmap/help/AnIndex
/usr/lib64/R/library/pheatmap/help/aliases.rds
/usr/lib64/R/library/pheatmap/help/paths.rds
/usr/lib64/R/library/pheatmap/help/pheatmap.rdb
/usr/lib64/R/library/pheatmap/help/pheatmap.rdx
/usr/lib64/R/library/pheatmap/html/00Index.html
/usr/lib64/R/library/pheatmap/html/R.css
