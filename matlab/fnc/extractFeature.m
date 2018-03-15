%
% extractFeature        - generates a biometric template from an iris in an
% eye image.
%
% Arguments:
%	eyeimage_filename   - the file name of the eye image
%
% Output:
%	template		    - the binary iris biometric template
%	mask			    - the binary iris noise mask
%

function [template, mask] = extractFeature(eyeimage_filename)
%% Setup
% Normalisation parameters
radial_res = 20;
angular_res = 240;

% Feature encoding parameters
nscales=1;
minWaveLength=18;
mult=1;
sigmaOnf=0.5;


%% Perform segmentation
eyeimage = imread(eyeimage_filename);
[circleiris, circlepupil, imagewithnoise] = segmentiris(eyeimage);


%% Perform normalization
[polar_array, noise_array] = normaliseiris(imagewithnoise, ...
    circleiris(2), circleiris(1), circleiris(3), ...
    circlepupil(2), circlepupil(1), circlepupil(3), ...
    eyeimage_filename, radial_res, angular_res);


%% Perform feature encoding
[template, mask] = encode(polar_array, noise_array, nscales, minWaveLength, mult, sigmaOnf); 


end

