export class Version {
  static VERSIONS = [
    {'id': 'red-blue', 'label': 'Red / Blue', 'generation': 1},
    {'id': 'yellow', 'label': 'Yellow', 'generation': 1},
    {'id': 'gold-silver', 'label': 'Gold / Silver', 'generation': 2},
    {'id': 'crystal', 'label': 'Crystal', 'generation': 2},
    {'id': 'ruby-sapphire', 'label': 'Ruby / Sapphire', 'generation': 3},
    {'id': 'emerald', 'label': 'Emerald', 'generation': 3},
    {'id': 'firered-leafgreen', 'label': 'FireRed / LeafGreen', 'generation': 3},
    {'id': 'diamond-pearl', 'label': 'Diamond / Pearl', 'generation': 4},
    {'id': 'platinum', 'label': 'Platinum', 'generation': 4},
    {'id': 'heartgold-soulsilver', 'label': 'HeartGold / SoulSilver', 'generation': 4},
    {'id': 'black-white', 'label': 'Black / White', 'generation': 5},
    {'id': 'black-2-white-2', 'label': 'Black 2 / White 2', 'generation': 5},
    {'id': 'x-y', 'label': 'X / Y', 'generation': 6},
    {'id': 'omega-ruby-alpha-sapphire', 'label': 'Omega Ruby / Alpha Sapphire', 'generation': 6},
    {'id': 'sun-moon', 'label': 'Sun / Moon', 'generation': 7},
    {'id': 'ultra-sun-ultra-moon', 'label': 'Ultra Sun / Ultra Moon', 'generation': 7}
  ];

  static get latest() {
    return Version.VERSIONS[Version.VERSIONS.length - 1]['id'];
  }

  static get ids() {
    return Version.VERSIONS.map(o => o.id);
  }

  static isLesserOrEqual(first, second) {
    const versions = Version.ids;
    return versions.indexOf(first) <= versions.indexOf(second);
  }
}
