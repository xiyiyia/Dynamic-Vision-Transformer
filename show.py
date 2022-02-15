import csv
import matplotlib.pyplot as plt

x = [0.49848031997680664, 0.5401372909545898, 0.5904931426048279, 0.6472992897033691, 0.7095174789428711, 0.7781971096992493, 0.8511193990707397, 0.9269490242004395, 1.0009031295776367, 1.075273036956787, 1.1469907760620117, 1.2189648151397705, 1.2923734188079834, 1.3634543418884277, 1.4280792474746704, 1.4899520874023438, 1.5536651611328125, 1.6110005378723145, 1.6692728996276855, 1.7248846292495728, 1.7777197360992432, 1.826409101486206, 1.8739533424377441, 1.9145554304122925, 1.9563630819320679, 1.998307228088379, 2.0395219326019287, 2.076345443725586, 2.113563060760498, 2.145885467529297, 2.1807520389556885, 2.213423252105713, 2.245326519012451, 2.2747867107391357, 2.3039114475250244, 2.3324642181396484, 2.359678030014038, 2.3855457305908203, 2.4101803302764893, 2.4325673580169678, 2.4573636054992676, 2.479761838912964, 2.500297784805298, 2.5205631256103516, 2.541318893432617, 2.5595929622650146, 2.5780599117279053, 2.5922975540161133, 2.60778546333313, 2.6226673126220703, 2.639995574951172, 2.655205249786377, 2.6723694801330566, 2.6866884231567383, 2.7014966011047363, 2.714423656463623, 2.72708797454834, 2.7412824630737305, 2.7525694370269775]
y = [69.614, 70.464, 71.372, 72.298, 73.148, 74.078, 74.83, 75.598, 76.23, 76.782, 77.29, 77.738, 78.128, 78.458, 78.688, 78.874, 79.048, 79.218, 79.346, 79.446, 79.544, 79.616, 79.656, 79.708, 79.748, 79.774, 79.806, 79.84, 79.862, 79.886, 79.908, 79.918, 79.924, 79.932, 79.944, 79.952, 79.956, 79.958, 79.964, 79.972, 79.972, 79.97, 79.972, 79.972, 79.972, 79.972, 79.972, 79.972, 79.974, 79.978, 79.98, 79.98, 79.98, 79.984, 79.984, 79.984, 79.986, 79.986, 79.986]

fig, ax = plt.subplots()  # figsize=(6, 2))
ax.plot(y, x, label="acc-FLOPs")
# ax.grid(color='dimgray', linestyle='--')  # linestyle='--')
ax.set_ylabel('FLOPs')
ax.set_xlabel('acc')
ax.set_title('ImageNet21k')
# plt.ylim((0,0.6))
# ax.legend()
plt.show()


ctl_t = []
csvFile = open('complete_time.csv', "r")
spamreader = csv.reader(csvFile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
for i in spamreader:
    if len(i) != 0:
        ctl_t.append(i)
    # break

# ctl.sort()
for i in range(len(ctl_t)):
    for j in range(len(ctl_t[i])):
        ctl_t[i][j] = float(ctl_t[i][j])
    ctl_t[i].sort()

per = [i for i in range(len(ctl_t[11]))]
# for i in range(len(ctl)):
#     per.append((i + 1.0) / len(ctl))
fig, ax = plt.subplots()  # figsize=(6, 2))
ax.plot(per, ctl_t[11], label="complete time")
# ax.grid(color='dimgray', linestyle='--')  # linestyle='--')
ax.set_ylabel('s')
ax.set_xlabel('img')
ax.set_title('ImageNet21k')
# plt.ylim((0,0.6))
# ax.legend()
plt.show()

# for ctl in ctl_t:
#     per = [i for i in range(len(ctl))]
#     # for i in range(len(ctl)):
#     #     per.append((i + 1.0) / len(ctl))
#     fig, ax = plt.subplots()  # figsize=(6, 2))
#     ax.plot(per, ctl, label="complete time")
#     # ax.grid(color='dimgray', linestyle='--')  # linestyle='--')
#     ax.set_ylabel('s')
#     ax.set_xlabel('img')
#     ax.set_title('ImageNet21k')
#     # plt.ylim((0,0.6))
#     # ax.legend()
#     plt.show()