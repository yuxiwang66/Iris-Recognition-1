%
%	Date: Nov 11, 2017
%
%	Description:
%		Match the extracted feature with database and give the result.
%
%	Input:
%		template_extr 	- Extracted feature from the iris image.
%		mask_extr
%		threshold 		- Threshold of distance.
%
%	Output:
%		id_acc 			- ID of the matched account, 0 if not, -1 if error.
%
function id_acc = matching(template_extr, mask_extr, threshold)
%% Get the number of accounts in the database
files = dir('template-database/*.mat');
numfile = length(files);
if numfile == 0
	id_acc = -1;
	return
end


%% Calculate the Hamming distance bw extracted feature with the database
hm_dist = zeros(1, numfile);
for i = 1 : numfile
	% Load each account
	clear template mask name exinfo
	load(['template-database/', num2str(i), '.mat'])

	% Calculate the Hamming distance
	template_extr = reshape(template_extr, 20, 480);
	mask_extr = reshape(mask_extr, 20, 480);
	template = reshape(template, 20, 480);
	mask = reshape(mask, 20, 480);
	hm_dist(1,i) = gethammingdistance(template_extr, mask_extr, template, mask, 1);
end


%% Threshold and give the result ID
id_acc = find(hm_dist <= threshold);
if length(id_acc) < 1
	id_acc = 0;
else if length(id_acc) > 1
	id_acc = -1;
end


end

