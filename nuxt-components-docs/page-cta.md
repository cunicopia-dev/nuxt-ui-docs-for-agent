<!-- source: https://ui.nuxt.com/components/page-cta --> # PageCTAPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageCTA.vue)

A call to action section to display in your pages.

## Usage

The PageCTA component provides a flexible way to display a call to action in
your pages with an illustration in the default slot.

## Trusted and supported by our amazing community

Preview the latest Tailwind CSS v4 and get started with Nuxt UI v3.

Get startedLearn more

![Illustration](https://picsum.photos/640/616)

Use it inside a [PageSection](/components/page-section) component or directly
in your page:

    
    
    <template>
      <UPageHero />
    
      <UPageCTA class="rounded-none" />
    
      <UPageSection />
    
      <UPageSection :ui="{ container: 'px-0' }">
        <UPageCTA class="rounded-none sm:rounded-xl" />
      </UPageSection>
    
      <UPageSection />
    </template>
    

Use `px-0` and `rounded-none` classes to make the CTA fill the edge of the
page on mobile.

### Title

Use the `title` prop to set the title of the CTA.

title

## Trusted and supported by our amazing community

    
    
    <template>
      <UPageCTA title="Trusted and supported by our amazing community" />
    </template>
    

### Description

Use the `description` prop to set the description of the CTA.

description

## Trusted and supported by our amazing community

We've built a strong, lasting partnership. Their trust is our driving force,
propelling us towards shared success.

    
    
    <template>
      <UPageCTA
        title="Trusted and supported by our amazing community"
        description="We've built a strong, lasting partnership. Their trust is our driving force, propelling us towards shared success."
      />
    </template>
    

### Links

Use the `links` prop to display a list of [Button](/components/button) under
the description.

## Trusted and supported by our amazing community

We've built a strong, lasting partnership. Their trust is our driving force,
propelling us towards shared success.

Get startedLearn more

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        color: 'neutral'
      },
      {
        label: 'Learn more',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageCTA
        title="Trusted and supported by our amazing community"
        description="We've built a strong, lasting partnership. Their trust is our driving force, propelling us towards shared success."
        :links="links"
      />
    </template>
    

### Variant

Use the `variant` prop to change the style of the CTA.

variant

soft

## Trusted and supported by our amazing community

We've built a strong, lasting partnership. Their trust is our driving force,
propelling us towards shared success.

Get startedLearn more

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        color: 'neutral'
      },
      {
        label: 'Learn more',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageCTA
        title="Trusted and supported by our amazing community"
        description="We've built a strong, lasting partnership. Their trust is our driving force, propelling us towards shared success."
        variant="soft"
        :links="links"
      />
    </template>
    

You can apply the `light` or `dark` class to the `links` slot when using the
`solid` variant to reverse the colors.

### Orientation

Use the `orientation` prop to change the orientation with the default slot.
Defaults to `vertical`.

orientation

horizontal

## Trusted and supported by our amazing community

We've built a strong, lasting partnership. Their trust is our driving force,
propelling us towards shared success.

Get startedLearn more

![Illustration](https://picsum.photos/640/728)

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        color: 'neutral'
      },
      {
        label: 'Learn more',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageCTA
        title="Trusted and supported by our amazing community"
        description="We've built a strong, lasting partnership. Their trust is our driving force, propelling us towards shared success."
        orientation="horizontal"
        :links="links"
      >
        <img
          src="https://picsum.photos/640/728"
          width="320"
          height="364"
          alt="Illustration"
          class="w-full rounded-lg"
        />
      </UPageCTA>
    </template>
    

### Reverse

Use the `reverse` prop to reverse the orientation of the default slot.

orientation

horizontal

reverse

true

## Trusted and supported by our amazing community

We've built a strong, lasting partnership. Their trust is our driving force,
propelling us towards shared success.

Get startedLearn more

![Illustration](https://picsum.photos/640/728)

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'Get started',
        color: 'neutral'
      },
      {
        label: 'Learn more',
        color: 'neutral',
        variant: 'subtle',
        trailingIcon: 'i-lucide-arrow-right'
      }
    ])
    </script>
    
    <template>
      <UPageCTA
        title="Trusted and supported by our amazing community"
        description="We've built a strong, lasting partnership. Their trust is our driving force, propelling us towards shared success."
        orientation="horizontal"
        reverse
        :links="links"
      >
        <img
          src="https://picsum.photos/640/728"
          width="320"
          height="364"
          alt="Illustration"
          class="w-full rounded-lg"
        />
      </UPageCTA>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`reverse`| `false`| `boolean`  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`  
`title`| | ` string`  
`description`| | ` string`  
`variant`| `'outline'`| ` "solid" | "outline" | "soft" | "subtle" | "naked"`  
`links`| | ` ButtonProps[]`Display a list of Button under the description. `{ size: 'lg' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; wrapper?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; links?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`title`| `{}`  
`description`| `{}`  
`links`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageCTA: {
          slots: {
            root: 'relative isolate rounded-xl overflow-hidden',
            container: 'flex flex-col lg:grid px-6 py-12 sm:px-12 sm:py-24 lg:px-16 lg:py-24 gap-8 sm:gap-16',
            wrapper: '',
            title: 'text-3xl sm:text-4xl text-pretty tracking-tight font-bold text-highlighted',
            description: 'text-base sm:text-lg text-muted',
            links: 'mt-8 flex flex-wrap gap-x-6 gap-y-3'
          },
          variants: {
            orientation: {
              horizontal: {
                container: 'lg:grid-cols-2 lg:items-center',
                description: 'text-pretty'
              },
              vertical: {
                container: '',
                title: 'text-center',
                description: 'text-center text-balance',
                links: 'justify-center'
              }
            },
            reverse: {
              true: {
                wrapper: 'lg:order-last'
              }
            },
            variant: {
              solid: {
                root: 'bg-inverted text-inverted',
                title: 'text-inverted',
                description: 'text-dimmed'
              },
              outline: {
                root: 'bg-default ring ring-default',
                description: 'text-muted'
              },
              soft: {
                root: 'bg-elevated/50',
                description: 'text-toned'
              },
              subtle: {
                root: 'bg-elevated/50 ring ring-default',
                description: 'text-toned'
              },
              naked: {
                description: 'text-muted'
              }
            },
            title: {
              true: {
                description: 'mt-6'
              }
            }
          },
          defaultVariants: {
            variant: 'outline'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            pageCTA: {
              slots: {
                root: 'relative isolate rounded-xl overflow-hidden',
                container: 'flex flex-col lg:grid px-6 py-12 sm:px-12 sm:py-24 lg:px-16 lg:py-24 gap-8 sm:gap-16',
                wrapper: '',
                title: 'text-3xl sm:text-4xl text-pretty tracking-tight font-bold text-highlighted',
                description: 'text-base sm:text-lg text-muted',
                links: 'mt-8 flex flex-wrap gap-x-6 gap-y-3'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center',
                    description: 'text-pretty'
                  },
                  vertical: {
                    container: '',
                    title: 'text-center',
                    description: 'text-center text-balance',
                    links: 'justify-center'
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'lg:order-last'
                  }
                },
                variant: {
                  solid: {
                    root: 'bg-inverted text-inverted',
                    title: 'text-inverted',
                    description: 'text-dimmed'
                  },
                  outline: {
                    root: 'bg-default ring ring-default',
                    description: 'text-muted'
                  },
                  soft: {
                    root: 'bg-elevated/50',
                    description: 'text-toned'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default',
                    description: 'text-toned'
                  },
                  naked: {
                    description: 'text-muted'
                  }
                },
                title: {
                  true: {
                    description: 'mt-6'
                  }
                }
              },
              defaultVariants: {
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            pageCTA: {
              slots: {
                root: 'relative isolate rounded-xl overflow-hidden',
                container: 'flex flex-col lg:grid px-6 py-12 sm:px-12 sm:py-24 lg:px-16 lg:py-24 gap-8 sm:gap-16',
                wrapper: '',
                title: 'text-3xl sm:text-4xl text-pretty tracking-tight font-bold text-highlighted',
                description: 'text-base sm:text-lg text-muted',
                links: 'mt-8 flex flex-wrap gap-x-6 gap-y-3'
              },
              variants: {
                orientation: {
                  horizontal: {
                    container: 'lg:grid-cols-2 lg:items-center',
                    description: 'text-pretty'
                  },
                  vertical: {
                    container: '',
                    title: 'text-center',
                    description: 'text-center text-balance',
                    links: 'justify-center'
                  }
                },
                reverse: {
                  true: {
                    wrapper: 'lg:order-last'
                  }
                },
                variant: {
                  solid: {
                    root: 'bg-inverted text-inverted',
                    title: 'text-inverted',
                    description: 'text-dimmed'
                  },
                  outline: {
                    root: 'bg-default ring ring-default',
                    description: 'text-muted'
                  },
                  soft: {
                    root: 'bg-elevated/50',
                    description: 'text-toned'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default',
                    description: 'text-toned'
                  },
                  naked: {
                    description: 'text-muted'
                  }
                },
                title: {
                  true: {
                    description: 'mt-6'
                  }
                }
              },
              defaultVariants: {
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageColumnsA responsive multi-column layout system for organizing content
side-by-side.](/components/page-columns)[PageFeatureA component to showcase
key features of your application.](/components/page-feature)

