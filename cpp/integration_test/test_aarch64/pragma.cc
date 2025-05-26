#ifndef __aarch64__
#pragma simd
#endif
void add_floats(float *a, float *b, float *c, float *d, float *e, int n)
{
	int i;

#ifndef __aarch64__
#pragma simd
#endif
	for (i=0; i<n; i++)
	{
		a[i] = a[i] + b[i] + c[i] + d[i] + e[i];
	}
}

#ifdef __aarch64__
#pragma simd // expect: PragmaIssue
#endif
void add_floats2(float *a, float *b, float *c, float *d, float *e, int n)
{
	int i;
#pragma simd // expect: PragmaIssue
	for (i=0; i<n; i++)
	{
		a[i] = a[i] + b[i] + c[i] + d[i] + e[i];
	}
}

#ifdef ppc64
#error 'ppc64 does not support simd instruction'
#else
#pragma simd // expect: PragmaIssue
#endif
void add_floats3(float *a, float *b, float *c, float *d, float *e, int n)
{
	int i;
#ifdef x86_64
#pragma simd
#endif
	for (i=0; i<n; i++)
	{
#ifndef ppc64
#pragma simd // expect: PragmaIssue
#endif
		a[i] = a[i] + b[i] + c[i] + d[i] + e[i];
	}
}
