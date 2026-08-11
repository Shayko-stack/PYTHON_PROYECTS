import cv2

cam=webcam(1);
wb=waitbar(0,"-","Name","Espera...","createCancelBtn","delete(gcbf)");
i=0;
while true
    img0=snapshot(cam);
    img=imsubtract(img0(:,:,2),rgb2gray(img0));
    bw=im2bw(img,0.15);
    %img=im2bw(img);
    bw=medfilt2(bw);
    bw=imopen(bw,strel("disk",1));
    bw=bwareaopen(bw, 3000);
    bw=imfill(bw,"holes");
    [L N]=bwlabel(bw);

    prop=regionprops(L);

    imshow(img0);
for n=1:N
c=round(prop(n).Centroid);
rectangle("Position",prop(n).BoundingBox,"EdgeColor","g","linewidth",2);
text(c(1),c(2),strcat("X:",num2str(c(1)), "Y:",num2str(c(2))),"color","green");
end

    if ~ishandle(wb)
        break
    else
        waitbar(i/10,wb,["num:" num2str(i)])
    end
   
    
    i=i+1;
    pause(0.001);
end
clear cam;
