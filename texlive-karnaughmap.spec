%global tl_name karnaughmap
%global tl_revision 36989

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Typeset Karnaugh maps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/karnaughmap
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaughmap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaughmap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaughmap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an easy to use interface to typeset Karnaugh maps
using TikZ. Though similar to the karnaugh macros, it provides a key-
value system to customize karnaughmaps and a proper LaTeX package.

