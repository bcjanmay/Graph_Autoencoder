from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import yaml
from model.pytorch.supervisor import GTSSupervisor, GAETSSupervisor
from lib.utils import load_graph_data

def main(args):
    with open(args.config_filename) as f:
        supervisor_config = yaml.load(f)
        save_adj_name = args.config_filename[11:-5]
        if args.model_name == "GTS":
            supervisor = GTSSupervisor(save_adj_name, temperature=args.temperature, **supervisor_config)
        elif args.model_name == "GAETS":
            supervisor = GAETSSupervisor(save_adj_name, temperature=args.temperature, **supervisor_config)
        else:
            raise Exception("Model {} is not implemented yet".format(args.model_name))
        supervisor.train()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_filename', default='data/model/para_la.yaml', type=str,
                        help='Configuration filename for restoring the model.')
    parser.add_argument('--use_cpu_only', default=False, type=bool, help='Set to true to only use cpu.')
    parser.add_argument('--temperature', default=0.5, type=float, help='temperature value for gumbel-softmax.')
    parser.add_argument('--model_name', default="GTS", type=str, help='Model name is GTS or GAETS')
    args = parser.parse_args()
    main(args)