Name:		texlive-karnaughmap
Version:	36989
Release:	2
Summary:	Typeset Karnaugh maps
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/karnaughmap
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaughmap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaughmap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaughmap.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an easy to use interface to typeset
Karnaugh maps using TikZ. Though similar to the karnaugh
macros, it provides a key-value system to customize
karnaughmaps and a proper LaTeX package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/karnaughmap
%{_texmfdistdir}/tex/latex/karnaughmap
%doc %{_texmfdistdir}/doc/latex/karnaughmap

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
