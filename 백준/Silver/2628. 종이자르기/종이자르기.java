import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int [] slice_w = new int[w+1];
        int [] slice_h = new int[h+1];
        int inputCount = Integer.parseInt(br.readLine());
        int wFlag = 0;
        int hFlag = 0;
        for(int i = 0; i < inputCount; i++) {
            st = new StringTokenizer(br.readLine());
            int flag = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());
            if(flag == 1) {
                wFlag = 1;
                slice_w[value] = 1;
            } else {
                hFlag = 1;
                slice_h[value] = 1;
            }
        }

        int tmp = 0;
        int maxW = 0;
        int maxH = 0;

        if(wFlag == 1) {
            for(int i = 1; i < slice_w.length; i++) {
                tmp++;
                if(slice_w[i] == 1 || i == slice_w.length - 1) {
                    if(maxW < tmp) maxW = tmp;
                    tmp = 0;
                }
            }
        }
        else {
            maxW = w;
        }

        tmp = 0;
        if(hFlag == 1) {
            for(int i = 1; i < slice_h.length; i++) {
                tmp++;
                if(slice_h[i] == 1 || i == slice_h.length - 1) {
                    if(maxH < tmp) maxH = tmp;
                    tmp = 0;
                }
            }
        } else {
            maxH = h;
        }
        System.out.println(maxW * maxH);
    }
}