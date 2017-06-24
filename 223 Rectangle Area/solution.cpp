class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int leng = max(0,min(C,G)-max(A,E));
        int width = max(0,min(D,H)-max(B,F));
        return (C-A)*(D-B)+(G-E)*(H-F)-leng*width;
    }
};