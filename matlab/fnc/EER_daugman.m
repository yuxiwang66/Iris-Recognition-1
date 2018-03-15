%
% calculation of FRR and FAR
% same represents same subject distance result��diff represents different subject distance result
%

%% Clean
clear
clc
fprintf('>>> Start evaluating system performance...\n')
tic


%% Initialize
load result/HD_same_daughman.mat
load result/HD_diff_daughman.mat

thres = 0:0.01:1;
FAR = zeros(size(thres));
FRR = zeros(size(thres));


%% Calculte FAR and FRR
for k=1:length(thres)
    FAR(k) = sum(HD_diff(1,:) <= thres(k)) / size(HD_diff,2);
    FRR(k) = sum(HD_same(1,:) > thres(k)) / size(HD_same,2);    
end


%% Calculte EER
EER = 1;
for i = 1:length(thres)-1
    if FAR(i) == FRR(i)
        EER = FAR(i);
        break;
    elseif sign(FAR(i)-FRR(i))*sign(FAR(i+1)-FRR(i+1)) == -1
        EER = (FAR(i)+FAR(i+1)+FRR(i)+FRR(i+1))/4;
        break;
    else
        EER = 1;            
    end
end


%% Visualize
% Result parameters
ind_FAR = find(FAR);
ind_FRR = find(FRR);
fprintf('FAR_oriented: FAR=%e, FRR=%e\n', FAR(ind_FAR(1)), FRR(ind_FAR(1)))
fprintf('FRR_oriented: FAR=%e, FRR=%e\n', FAR(ind_FRR(end)), FRR(ind_FRR(end)))
fprintf('EER = %f\n', EER)
fprintf('\nProcess takes %f [s]\n\n', toc)

% Distribution of intra-class and inter-class
x = linspace(0, 1, 101);
dist_intra = hist(HD_same, x) / size(HD_same,2) * 100;
dist_inter = hist(HD_diff, x) / size(HD_diff,2) * 100;
figure(1), clf
plot(x, dist_intra, '-.r')
hold on
plot(x, dist_inter, '-b')
legend('intra-', 'inter-')
title('Distribution of intra- and inter-class')
xlabel('Normalized distance')
ylabel('Density%')
grid on
saveas(gcf, 'result/distribution-daughman', 'epsc')

% FRR versus FAR
figure(2), clf
semilogx(FAR, FRR)
xlabel('FAR')
ylabel('FRR')
title('FRR versus FAR')
grid on
saveas(gcf, 'result/FRR_FAR-daughman', 'epsc')

